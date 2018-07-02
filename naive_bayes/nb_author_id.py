#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from sklearn.naive_bayes import GaussianNB
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


clf = GaussianNB()
print("Started training")
t0 = time()
clf.fit(features_train, labels_train)
print("Training time is {0}".format(round(time()-t0, 3)))
print("Started predicting")
t0 = time()
results = clf.predict(features_test)
print("Predicting time is {0}".format(round(time()-t0, 3)))
accuracy = clf.score(features_test, labels_test)
print("Accuracy is {0}".format(round(accuracy, 3)))