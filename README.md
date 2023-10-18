# Movie Reviews Prediction Modeling Project
This is a final project for ADS509: Text Based Analysis

[Business Case Presentation](https://docs.google.com/presentation/d/148sGmTrqkthCvEs_wwvh8I8FSqE4T2kByE2uJKcvSPE/edit?usp=sharing)


#### -- Project Status: [Completed]

## Project Intro


### Team 7
* Jacqueline Vo
* Connie Chow

### Methods Used
* Data preprocessing
* Exploratory Data Analysis
* Data Visualization
* Predictive Modeling


### Technologies
* Python
* Pandas, jupyternotebook


## Project Description
 


## Needs of this project

- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting
- presentation
- voice recordings

## Required Python Packages
* import pandas as pd
* import matplotlib
* import matplotlib.pyplot as plt
* import numpy as np
* from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
* import seaborn as sns
* from sklearn.experimental import enable_iterative_imputer
* from sklearn.impute import IterativeImputer
* from sklearn import linear_model
* from sklearn.impute import SimpleImputer
* from sklearn.neighbors import KNeighborsClassifier
* from collections import defaultdict
* from scipy import stats
* from sklearn.cluster import KMeans
* from pandas.api.types import CategoricalDtype
* %matplotlib inline
* from sklearn.ensemble import RandomForestClassifier
* import statsmodels.api as sm
* import statsmodels.tools.tools as stattools
* from sklearn.metrics import confusion_matrix
* from sklearn.tree import DecisionTreeClassifier, export_graphviz
* from sklearn.tree import plot_tree
* import random
* from sklearn.model_selection import train_test_split
* from sklearn.naive_bayes import MultinomialNB
* from sklearn.linear_model import LogisticRegression
* from sklearn.model_selection import KFold, cross_val_score
* from sklearn import tree

## Getting Started

1. Clone this repo using raw data.
2. add code and push new code into repo. To ensure cohesive code make sure to run all cells prior to upload. 
3. Use ###### flags for output

## Featured Notebooks/Analysis/Deliverables



## Data Pre-Processing
* SimpleImputer class was used to impute missing column values on a case-by-case basis
* Boxplots were used to detect outliers - Number of Referrals, Avg Monthly GB Download, Total Refunds, Total Long Distance Charges, Total Revenue
* Dataset was rebalanced for equal number of Churn and Not Churned customers


## Exploratory Data Analysis

Univariate Analysis

Multivariate Analysis



## Features Selection
* Refer to chi-square test in this file
* Pairwise Correlation
* Correlation to Target 
* Test for Column Variance


## Modeling & Evaluation
* Logistic Regression
* Decision Tree
* Naïve Bayes
* Random Forest
* K-means
* CART
* C5.0
