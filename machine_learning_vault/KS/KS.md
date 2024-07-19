#ks #kolmogorov-smirnov #binary_classification
# Kolmogorov-Smirnov (KS)

## What is the KS test?

The Kolmogorov-Smirnov (KS) test is a non-parametric test used to compare two distributions. It can be used to:

1. Compare a sample with a reference probability distribution (one-sample KS test).
2. Compare two samples (two-sample KS test)

## Why use the KS test in Machine Learning?


In machine learning, the KS test is often used to evaluate the performance of models, particularly in binary classification problems. It **helps measure how well the model separates the positive and negative classes**. 

The KS statistic quantifies the maximum distance between the Cumulative Distribution Functions ([ECDF](ECDF.md)) of the predicted probabilities for the two classes.


## Steps to Understand the KS Test with an Example

Let's go through a step-by-step example.

