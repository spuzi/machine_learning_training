

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

Its simply the probability that a randomly chosen positive data point will have
a higher rank than a randomly chosen negative data point for your learning problem.



