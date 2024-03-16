import pandas as pd
import numpy as np
import os
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import RandomizedSearchCV

RANDOM_STATE_VALUE = 9
TEST_SIZE_VALUE = 0.2
LASSO_ALPHA_VALUE = 0.3
RANDOM_FOREST_REGRESSOR_CROSS_VALIDATION = 5


def read_rental_data():
    rental_data_path = os.path.join(
        os.getcwd(),
        "exercises",
        "predicting_movie_rental_duration",
        "rental_info.csv",
    )

    df_rental = pd.read_csv(rental_data_path)

    return df_rental


def calculate_rental_length_days(df_rental):
    """
    Calculate the rental length in days
    """

    # Parse from string to datetime
    df_rental[["rental_date", "return_date"]] = df_rental[
        ["rental_date", "return_date"]
    ].apply(pd.to_datetime)

    # Create a columns with the number of days that the client had the DVD.
    # Time difference between the rental day and the return date
    df_rental["rental_length_days"] = (
        df_rental["return_date"] - df_rental["rental_date"]
    )
    # Get only the days of differences, we can ignore the minutes, seconds...
    df_rental["rental_length_days"] = df_rental["rental_length_days"].dt.days

    return df_rental


def add_dummy_variables(df_rental):
    # Add dummy for deleted scenes
    df_rental["deleted_scenes"] = np.where(
        df_rental["special_features"].str.contains("Deleted Scenes"), 1, 0
    )

    # Add dummy for behind the scenes
    df_rental["behind_the_scenes"] = np.where(
        df_rental["special_features"].str.contains("Behind the Scenes"), 1, 0
    )

    return df_rental


def select_features(df_rental):
    """
    Select the features for the model, avoid columns that leak data about
    the target

    Args:
        df_rental (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: The dataframe with the selected features
    """
    X = df_rental.drop(
        [
            "special_features",
            "rental_length_days",  # target variable
            "rental_date",  # date column
            "return_date",
        ],  # date column
        axis=1,
    )

    return X


def select_relevant_features(X, y):
    """
    Select the relevant features for the model using Lasso regression
    """
    lasso = Lasso(alpha=LASSO_ALPHA_VALUE, random_state=RANDOM_STATE_VALUE)
    lasso.fit(X, y)
    lasso_coef = lasso.coef_

    # Select the features where the coefficient is greater than 0
    relevant_features = X.iloc[:, lasso_coef > 0].columns
    return list(relevant_features)


def ols_linear_regression(X_train, y_train):
    """
    Train a linear regression model
    """

    linear_regression = LinearRegression()
    linear_regression.fit(X_train, y_train)
    linear_regression_score = linear_regression.score(X_train, y_train)
    y_pred = linear_regression.predict(X_train)
    mse = mean_squared_error(y_train, y_pred)

    return {
        "model_name": "Linear Regression",
        "model": linear_regression,
        "score": linear_regression_score,
        "mse": mse,
    }


def random_forest_regression(X_train, y_train):
    """
    Train a random forest regression model
    """
    # Lets perform a random search to find the best parameters
    param_grid = {
        "n_estimators": np.arrange(1, 101, 1),
        "max_depth": np.arrange(1, 11, 1),
    }

    random_search = RandomizedSearchCV(
        RandomForestRegressor(),
        param_distributions=param_grid,
        random_state=RANDOM_STATE_VALUE,
        cv=RANDOM_FOREST_REGRESSOR_CROSS_VALIDATION,
    )

    random_search.fit(X_train, y_train)
    best_params = random_search.best_params_

    # Once we know the best parameters, we can train the model
    rf = RandomForestRegressor(
        n_estimators=best_params["n_estimators"],
        max_depth=best_params["max_depth"],
        random_state=RANDOM_STATE_VALUE,
    )
    rf.fit(X_train, y_train)
    random_forest_score = rf.score(X_train, y_train)
    y_pred = rf.predict(X_train)
    mse = mean_squared_error(y_train, y_pred)

    return {
        "model_name": "Random Forest Regression",
        "model": rf,
        "score": random_forest_score,
        "mse": mse,
    }
