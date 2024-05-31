

## Introduction XGB
https://campus.datacamp.com/courses/extreme-gradient-boosting-with-xgboost/classification-with-xgboost?ex=1
XGBoost its an implementation of Gradient Boosting, 
In order to understand XGBoost, we need to have some knowledge on the broader
topics of supervised classification, decision tress and boosting.

To begin, lets briefly review what supervised learning is and the kind of 
problems its methods can be applied to.

Supervised learning is the kind of learning problem that XGBoost is applied to, 
which relies on labeled data. That is, you have some understanding of the
past behavior of the problem you're trying to solve or what you're trying 
to predict.

For example, assessing whether a specific image contains a person's face is
a classification problem.
Here the training data are images converted into vectors of pixel values, and
the labels are either 1 when the image contains a face or 0 when the image 
doesn't contain a face.
Given this, there are two kinds of supervised learning problems that account
for the vast majority of use cases: classification and regression.


## Supervised Learning: Classification Problems
Classification problems involve predicting either binary or multi-class
outcomes.
For example, predicting whether a person will purchase an insurance package
given some quote is a binary supervised learning problem.
And predicting whether a picture contains one of several species of birds
is a multi-class supervised learning problem.
When dealing with binary supervised learning problems, the AUC (Area Under
the Receive Operating Characteristic (ROC)) is the most versatile and common
evaluation metric used to judge the quality of a binary classification model.

[Logictic Regression and the ROC curve](../supervised_learning_with_scikit-learn/06_logistic_regression_and_the_roc_curve/06_logistic_regression_and_the_roc_curve.md)

Its simply the probability that a randomly chosen positive data point will have
a higher rank than a randomly chosen negative data point for your learning problem.

When dealing with multiclass classification problems, its common to use the
accuracy score (higher is better) and to look at the overall confusion matrix
to evaluate the quality of a model

$$ accuracy = \frac{t_p + t_n}{t_p + t_n + f_p + f_n}$$

[Measuring how good is your model](../supervised_learning_with_scikit-learn/05_how_good_is_your_model/05_how_good_is_your_model.md)

Some common algorithms for classification problems include logistic regression
and decision trees.

All supervised learning problems, including classification problems, require 
that the data is structured as a table of feature vectors, where the features
themselves (also called attributes or predictors) are either numerical or
categorical.

Furthermore, it is usually the case that the numeric features are scaled to 
aid in either feature interpretation or to ensure that the model can be trained
properly.

For example, numeric feature scaling is essential to ensure property trained
support vector machine models.

Categorical features are also almost always encoded before applying supervised
learning algorithms, most commonly using one-hot encoding.

Finally, other kind of supervised learning problems exist, so I'll mention
them briefly.

Ranking problems involve predicting an ordering on a set of choices (like
google search suggestions) and recommendation problems include recommending 
and item or a set or items to a user based on his/her consumption history 
and profile (like Netflix).

https://campus.datacamp.com/courses/extreme-gradient-boosting-with-xgboost/classification-with-xgboost?ex=2
## Exercise 
Which of these is a classification problem?<br>
Given below are 4 potential machine learning problems you might encounter in the wild. Pick the one that is a classification problem.

- [ ] Given past performance of stocks and various other financial data, predicting the exact price of a given stock (Google) tomorrow.
    - Not quite. This is an example of a regression problem, because we are predicting a continuous quantity.

- [ ] Given a large dataset of user behaviors on a website, generating an informative segmentation of the users based on their behaviors.
    - There's nothing to predict here, this is an unsupervised (clustering) problem.

- [X] Predicting whether a given user will click on an ad given the ad content and metadata associated with the user.

- [ ] Given a user's past behavior on a video platform, presenting him/her with a series of recommended videos to watch next.
    - Incorrect. This problem involves ranking entities and returning the highest ranked ones (in order) to the user.


https://campus.datacamp.com/courses/extreme-gradient-boosting-with-xgboost/classification-with-xgboost?ex=3
## Exercise
Which of these is a binary classification problem?<br>
Great! A classification problem involves predicting the category a given data point belongs to out of a finite set of possible categories. Depending on how many possible categories there are to predict, a classification problem can be either binary or multi-class. Let's do another quick refresher here. Your job is to pick the binary classification problem out of the following list of supervised learning problems.


- [X] Predicting whether a given image contains a cat.
- [ ] Predicting the emotional valence of a sentence (Valence can be positive, negative, or neutral).
    - There are 3 categories to choose from here. Try again.
- [ ] Recommending the most tax-efficient strategy for tax filing in an automated accounting system.
    - This smells like a recommendation problem, not a classification problem.
- [ ] Given a list of symptoms, generating a rank-ordered list of most likely diseases.
    - Incorrect. This is a recommendation problem.

## Introduction
XGBoots its a popular machine learning library for good reason. It was developed
originally as a C++ command-line application. After winning a popular machine
learning competition, the package started being adopted wither the ML 
community. As a result, bindings, or functions that tapped into the core C++
code, started appearing in a variety of other languages, including Python, R, 
Scala, and Julia.
We will cover the Python API in this course.

### What makes XGBoost so popular?
Its speed and performance, because the core XGBoost algorithm is parallelizable
it can harness all the processing power of modern multi-core computers.
Furthermore, it is parallelizable onto GPU's and across networks of computers, 
making it feasible to train models on very large datasets on the order of 
hundreds of millions training examples.

However, XGBoost's speed isn't the package's real draw. Ultimately, a fast but
poorly performing machine learning algorithm is not going to have a wide 
adoption within the community. 
What makes XGBoost so popular is that it consistently outperforms almost all 
others single-algorithms methods in machine learning competitions and has been
shown to achieve state-of-the-art performance on a variety of benchmark 
machine learning datasets.

Here's an example of how we can use XGBoost using classification problem.

```python
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class_data = pd.read_csv("classification_data.csv")

# Separate between features and target
X, y = class_data.iloc[:, :-1], class_data.iloc[:, -1]

# Separate data between train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123)

# Instantiate our XGBoost Classifier
xg_cl = xgb.XGBClassifier(
    objective='binary:logistic', 
    n_estimators =10, 
    seed=123
)

# Train the model
xg_cl.fix(X_train, y_train)

# Predict on the test set
preds = xg_cl.predict(X_test)

# Calculate how good our model is
accuracy = float(np.sum(preds == y_test))/y_test.shape[0]

print("accuracy :%f" % (accuracy))
# accuracy: 0.78
```



