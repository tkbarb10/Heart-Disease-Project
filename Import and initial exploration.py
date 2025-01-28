# === Import modules ===

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo

# === Download data from UCI repository ===
  
# fetch dataset 
heart_disease = fetch_ucirepo(id=45) 
  
# data (as pandas dataframes) 
X = heart_disease.data.features 
y = heart_disease.data.targets 
  
# metadata 
metadata = heart_disease.metadata 
  
# variable information 
print(heart_disease.variables) 

# Copy to experiment on
X_copy = X.copy()
y_copy = y.copy()

# === Send metadata to a txt document ===

# with open('heart disease metadata', 'w') as file:
#     for column, description in metadata.items():
#         file.write(f"{column}: {description}\n")

"""
Last item is additional info and is another dictionary of info
so deleting that and creating a separate txt document
"""

# === Initial exploration ===

X.head()
y.head()

X.shape


X.info()
y.info()

pd.set_option('display.max_columns', None)
X.describe()

"""
Only a few of the variables are relevant since most are
technically categorical variables that have been encoded
"""

X.isna().sum()

"""
4 NA values in ca and 2 in thal so we'll look at those. 
Only a couple, so best to delete them most likely
"""

y.isna().sum()

"""
No NA values in the target variable
"""

X.duplicated().sum()

"""
No duplicates to worry about
"""