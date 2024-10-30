# -*- coding: utf-8 -*-
"""course project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17l_bp8jFVk81pcRjE6yjSwT29TIxLpcq
"""

# Import necessary libraries for MNIST
from keras.datasets import mnist
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from skimage.feature import hog
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.model_selection import cross_validate
import seaborn as sns

# Load the dataset
(train_X, train_y), (test_X, test_y) = mnist.load_data()

# Print the shapes of each dataset split
print(f"Train data shape: {train_X.shape}")
print(f"Test data shape: {test_X.shape}")

# Plotting
plt.figure(figsize=(8, 8))
for i in range(16):
    plt.subplot(4, 4, i + 1)
    plt.imshow(train_X[i], cmap=plt.get_cmap('gray'))
plt.show()

def extract_hog_features(images):
    features = []
    for image in images:
      fd = hog(image, orientations=8, pixels_per_cell=(4, 4), cells_per_block=(2, 2))
      features.append(fd)
    return np.array(features)

train_X_hog = extract_hog_features(train_X)
test_X_hog = extract_hog_features(test_X)
# Plotting
train_X_hog.shape

accuracies = {}

knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(train_X_hog, train_y)

test_y_pred_knn = knn_classifier.predict(test_X_hog)
test_accuracy_knn = accuracy_score(test_y, test_y_pred_knn)
print(f"Test accuracy with KNN: {test_accuracy_knn}")
accuracies['knn'] = test_accuracy_knn

report_KNN = classification_report(test_y, test_y_pred_knn, output_dict=True)
print(sns.heatmap(pd.DataFrame(report_KNN).transpose(), annot=True, cmap = 'coolwarm'))

rf = RandomForestClassifier(n_estimators=50)
rf.fit(train_X_hog, train_y)

test_y_pred_rf = rf.predict(test_X_hog)
test_accuracy_rf = accuracy_score(test_y, test_y_pred_rf)
print(f"Test accuracy with Random Forest: {test_accuracy_rf}")
accuracies['Random Forest'] = test_accuracy_rf

report_RF = classification_report(test_y,test_y_pred_rf, output_dict=True)
print(sns.heatmap(pd.DataFrame(report_RF).transpose(), annot=True, cmap = 'coolwarm'))

dt = DecisionTreeClassifier()
dt.fit(train_X_hog, train_y)

test_y_pred_dt = dt.predict(test_X_hog)
test_accuracy_dt = accuracy_score(test_y, test_y_pred_dt)
print(f"Test accuracy with Decision Tree: {test_accuracy_dt}")
accuracies['Decision Tree'] = test_accuracy_dt

report_DT = classification_report(test_y,test_y_pred_dt, output_dict=True)
print(sns.heatmap(pd.DataFrame(report_DT).transpose(), annot=True, cmap = 'coolwarm'))

gn = GaussianNB()
gn.fit(train_X_hog, train_y)

test_y_pred_gn = gn.predict(test_X_hog)
test_accuracy_gn = accuracy_score(test_y, test_y_pred_gn)
print(f"Test accuracy with naive bayes : {test_accuracy_gn}")
accuracies['naive bayes'] = test_accuracy_gn

report_GN = classification_report(test_y,test_y_pred_gn, output_dict=True)
print(sns.heatmap(pd.DataFrame(report_GN).transpose(), annot=True, cmap = 'coolwarm'))

lg = LogisticRegression()
lg.fit(train_X_hog, train_y)

test_y_pred_lg = lg.predict(test_X_hog)
test_accuracy_lg = accuracy_score(test_y, test_y_pred_lg)
print(f"Test accuracy with Logistic Regression: {test_accuracy_lg}")
accuracies['Logistic Regression'] = test_accuracy_lg

report_lg = classification_report(test_y,test_y_pred_lg, output_dict=True)
print(sns.heatmap(pd.DataFrame(report_lg).transpose(), annot=True, cmap = 'coolwarm'))

print(accuracies)
res = [key for key in accuracies if all(accuracies[temp] <= accuracies[key] for temp in accuracies)]

print(f'The best algorithm is : {res}')

import matplotlib.pyplot as plt

from skimage.feature import hog
from skimage import data, exposure


image = data.cat()


fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True, channel_axis=-1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)
ax1.axis('off')
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Input image')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()

import matplotlib.pyplot as plt

from skimage.feature import hog
from skimage import data, exposure

for i in range(16):
  image = train_X[i]

  fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True, )

  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 2), sharex=True, sharey=True)
  ax1.axis('off')
  ax1.imshow(image, cmap=plt.cm.gray)
  ax1.set_title('Input image')

  # Rescale histogram for better display
  hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

  ax2.axis('off')
  ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
  ax2.set_title('Histogram of Oriented Gradients')
  plt.show()
