# === Deleting Missing Values ===

missing_indexes = X[X.isna().any(axis = 1)].index
X.dropna(inplace = True)

y.drop(missing_indexes, inplace = True)

# === Renaming columns ===

predictor_columns = X.columns

new_names = ['Age', 'Sex', 'Chest_Pain_Type', 'Resting_BP(mm HG)', 
             'Cholesterol(mg/dl)', 'Fasting_Blood_Sugar(> 120 mg/dl)',
             'Resting_ECG_Results', 'Max_HR', 'Exercise_Induced_Angina',
             'Old_Peak', 'ST_Slope', 'Number_of_Colored_Vessels',
             'Thallium_Stress_Test']

new_name_dict = dict(zip(predictor_columns, new_names))

X = X.rename(columns = new_name_dict)

# Changing column types to be represented more appropriately for classification

X.dtypes