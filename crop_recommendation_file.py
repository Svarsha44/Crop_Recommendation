# -*- coding: utf-8 -*-
"""Crop_recommendation_file.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i6yfaXg9tJtvTmXxasVlcXVpe1D4dZEj
"""

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings
import pickle

from google.colab import drive
drive.mount('/content/drive')

#Data reading
import numpy as np
import pandas as pd
path="/content/drive/MyDrive/CropRecommendation/Crop_recommendation.csv"
df=pd.read_csv(path)
df



x=df['label'].unique()
x

df['label'].value_counts()

df.shape
#data preprocessing

df.dtypes

df.isna().sum()

df.describe()

x=df.iloc[:,0:7]
y=df.iloc[:,-1]
x

accuracy = []

model_1=[]
out_name=[]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

sample_input= [[20,30,	2,	5,	30,	9	,100]]

a=list()

import math
class Multiple_regressor():
  def __init__(self):
    self.df = pd.read_csv('/content/drive/MyDrive/CropRecommendation/Crop_recommendation.csv')
    self.profits = pd.read_csv('/content/drive/MyDrive/CropRecommendation/profits.csv')
    pass

  def NearestNeighbors(self,test,kNeighhbors):

  #arr = np.zeros(df.shape[0],np.int)
    self.arr = list()
    for i,x in enumerate(self.df.values):
      #print(test,x)
      dist = np.linalg.norm(test - x[:-1])
      self.arr.append((dist,i))
    self.arr.sort()
    self.NearestClasses = list()
    for i,x in enumerate(self.arr[:kNeighhbors]):
      self.NearestClasses.append((i,self.df.iloc[x[1],-1]))
    self.prof_inv_ratio = dict()
    for i,x in enumerate(self.profits.values):
      self.prof_inv_ratio.update({x[0]:x[-1]/x[1]})
    self.display()

  def display(self):
        for x in self.NearestClasses:
          a=[x[1],self.prof_inv_ratio[x[1]]]
          print(a)



o=Multiple_regressor()
o.NearestNeighbors(sample_input[0],3)



pickle.dump(o,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
model.NearestNeighbors([90,42,43,20.879743,82.002,6.50,202.93],3)

