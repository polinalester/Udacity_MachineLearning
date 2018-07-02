#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

import numpy as np
from sklearn.svm import SVC
# clf = SVC(kernel='linear')
clf = SVC(kernel='rbf', C=10000.0)
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

# print("10th result is {0}".format(results[10]))
# print("26th result is {0}".format(results[26]))
# print("50th result is {0}".format(results[50]))

indices = np.where(results == 1)[0]
print("In class 1 there are {0} messages".format(len(indices)))
