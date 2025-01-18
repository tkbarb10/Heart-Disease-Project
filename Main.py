# === Import modules ===
import pandas
import numpy
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
X.dtypes

y.dtypes

predictor_columns = X.columns
