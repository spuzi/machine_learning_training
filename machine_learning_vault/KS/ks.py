
import numpy as np
import pandas as pd

from machine_learning_vault.ECDF.ecdf import calculate_ecdf

# Step 1: Prepare your data
# Suppose you have a binary classification model, and you have predicted 
# probabilities for the positive class and the actual labels for your test set.

# The probabilities that the model predicted
predicted_probabilities = [0.9, 0.8, 0.6, 0.4, 0.7, 0.2, 0.3, 0.1, 0.5, 0.55]
# The real target value 
actual_labels = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1]

predicted_probabilities = np.array(predicted_probabilities)
actual_labels = np.array(actual_labels)


# Step 2: Separate Predictions by Class
# Separate the predicted probabilities into two groups based on the actual labels.

positive_probabilities = predicted_probabilities[actual_labels == 1]
negative_probabilities = predicted_probabilities[actual_labels == 0]

# Step 3: Calculate the ECDF for feach group
# The Empirical Cumulative Distribution Function (ECDF) is a step function.
positive_x, positive_ecdf = calculate_ecdf(positive_probabilities)

negative_x, negative_ecdf = calculate_ecdf(negative_probabilities)
print("end")

