#!/usr/bin/env python3

# Backwards compatibility for python2
from __future__ import print_function

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

filename = "train.csv"
label_file = "train-labels.txt"
test_file = "test.csv"
prediction_output = "predictions.txt"

print("Program initialized...")

# Load the training features into a np array
features = np.loadtxt(filename, delimiter=',', dtype=np.uint8)
# Load the labels
with open(label_file) as f:
    labels = f.readlines()
# Strip any new line characters or extra spaces
labels = [x.strip() for x in labels]
# Convert to np array
labels = np.asarray(labels)

# Split data up into training and test data
X_train, X_test, y_train, y_test = train_test_split(features, labels)

print("Starting training...")
clf = LogisticRegression()
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Model has accuracy of " + str(score * 100) + "%")

print("Predicting over the Kaggle test set")
test_data = np.loadtxt(test_file, delimiter=',', dtype=np.uint8)
predictions = clf.predict(test_data)

with open(prediction_output, "w") as f:
    for prediction in predictions:
        print(prediction, file=f)
