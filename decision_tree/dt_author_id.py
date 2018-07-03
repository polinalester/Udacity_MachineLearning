#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn import tree

clf = tree.DecisionTreeClassifier(min_samples_split=40)
print("Started training")
t0 = time()
clf.fit(features_train, labels_train)
print("Training time is {0}".format(round(time()-t0, 3)))
print("Started predicting")
t0 = time()
results = clf.predict(features_test)
print("Predicting time is {0}".format(round(time()-t0, 3)))

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(labels_test, results)
print("Accuracy is {0}".format(round(accuracy, 3)))

print("Number of features is {0}".format(len(features_test[0])))