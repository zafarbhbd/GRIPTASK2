# -*- coding: utf-8 -*-
"""Sol3. DecisionTrees.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rIhVQnfHPGi_rkJT4p-8TWm5w4nk-PNn

# **The Spark Foundation**
**Graduate Rotational Internship Program**

**Data Science and Business Analytics**

# **Task 2**

# **Author: Abu Zafar**

### Workshop - Decision Trees

This workshop deals with understanding the working of decision trees.
"""

from google.colab import drive

drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

import warnings as wg
wg.filterwarnings('ignore')

import os

path = './drive/MyDrive/Data/Iris.csv'

data = pd.read_csv(path)

data

data.describe()

list(data.columns)

# Forming the iris dataframe
flower =pd.DataFrame(data)
flower_dataframe= flower.drop(columns=["Id", "Species"])
print(flower_dataframe.head(5))
print(flower_dataframe.tail(5))

within_cluster_ss = []
c_range = range(1,8)
for k in c_range:
  km = KMeans(n_clusters= k)
  km = km.fit(flower_dataframe)
  within_cluster_ss.append(km.inertia_)

plt.plot(c_range, within_cluster_ss, color = 'red')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('within clusters sum of squares')
plt.grid()
plt.show()

from sklearn.cluster import KMeans
model = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 500, n_init = 10, random_state = 0)
pred = model.fit_predict(flower_dataframe)

"""# **Data Visualization**"""

x = flower_dataframe.iloc[:,[0, 1, 2, 3]].values
plt.scatter(x[pred == 0, 0], x[pred == 0, 1], s = 25, c= 'Yellow', label = 'Iris-setosa')
plt.scatter(x[pred == 1, 0], x[pred == 1, 1], s = 25, c= 'Red', label = 'Iris-versicolor')
plt.scatter(x[pred == 2, 0], x[pred == 2, 1], s = 25, c= 'Green', label = 'Iris-virginica')
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],s = 100, c = 'Blue', label = 'Centroids')
plt.title('K-Means Cluster')
plt.legend()
plt.show()

"""**This way, we have predicted the optimal number of clusters and their visual representation.**"""

