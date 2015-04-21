# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:49:10 2015

@author: rachael
"""

"""

Let's use the glass identification dataset again.   We've previously run knn
on this dataset.  Now, let's try logistic regression.  Access the dataset at
http://archive.ics.uci.edu/ml/datasets/Glass+Identification.  Complete the 
following tasks or answer the following questions.


6. Create and fit a logistic regression model.
7. Make predictions with your new model.
8. Calculate the accuracy rate of your model and compare it to the null accuracy.
9. Generate a confusion matrix for your predictions.  Use this to calculate the
sensitivity and specificity of your model.
"""


import pandas as pd
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data',
                 names=['id','ri','na','mg','al','si','k','ca','ba','fe','glass_type'],
                 index_col='id')

import numpy as np
df['binary'] = df.glass_type.map({1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1})   

features = ['ri','na','mg','al','si','k','ca','ba','fe']    
X = df[features]             
y = df.binary

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test) 

print metrics.accuracy_score(y_test, y_pred)

1 - y_test.mean()

con_mat = metrics.confusion_matrix(y_test, y_pred)
print con_mat

true_neg = con_mat[0][0]
false_neg = con_mat[1][0]
true_pos = con_mat[1][1]
false_pos = con_mat[0][1]

sensitivity = float(true_pos)/(true_pos + false_neg)
print sensitivity

specificity = float(true_neg)/(true_neg + false_pos)
print specificity