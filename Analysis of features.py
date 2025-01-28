# === Univariate Analysis ===

# Start with Age

basic_stats = X_copy['Age'].describe()

IQR = basic_stats['75%'] - basic_stats['25%']

upper_bound = basic_stats['75%'] + 1.5*IQR
lower_bound = basic_stats['25%'] - 1.5*IQR

age_outliers = X_copy[X_copy['Age'] < lower_bound]['Age']

"""
No outliers for age
"""

mean = X_copy['Age'].mean()
median = X_copy['Age'].median()

"""
Plotting histogram with basic stats
"""

plt.figure(figsize = (10,6))

ax = sns.histplot(X['Age'], edgecolor = 'black')

for bar in ax.patches:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        int(height),
        ha = 'center', va = 'bottom', fontsize = 10, color = 'black'
    )

ax.axvline(
    mean, 
    color = 'red', 
    linestyle = 'dashed', 
    linewidth = 2,
    label = f'Mean: {mean: .2f}'
    )

ax.axvline(
    median,
    color = 'forestgreen',
    linestyle = 'dashed',
    linewidth = 2,
    label = f"Median: {median}"
)

plt.legend()

plt.show()

# Bar Chart of Sex

X_copy['Sex'] = X_copy['Sex'].astype('category')

plt.figure(figsize = (10, 6))

ax = sns.barplot(X_copy['Sex'], color = 'red', alpha = .7)
ax.set_yticklabels([label.get_text().title() for label in ax.get_yticklabels()])

plt.show()


# Chest Pain

new_values = {1: 'Typical', 2: 'Atypical', 3: "Non-Anginal", 4: 'Asymptomatic'}

X_copy['Chest_Pain_Type'] = X_copy['Chest_Pain_Type'].map(new_values)

sorted_order = X_copy['Chest_Pain_Type'].value_counts().index


plt.figure(figsize = (12, 6))

ax = sns.countplot(x = 'Chest_Pain_Type', data = X_copy, order = sorted_order)

ax.set_ylabel('Count')
ax.set_xlabel('Chest Pain Type')

plt.show()


# Resting bp

basic_stats = X_copy['Resting_BP(mm HG)'].describe()

mean = X_copy['Resting_BP(mm HG)'].mean()

IQR = basic_stats['75%'] - basic_stats['25%']

upper_bound = basic_stats['75%'] + 1.5*IQR
lower_bound = basic_stats['25%'] - 1.5*IQR

"""
Box plot
"""

ax = sns.boxplot(
    x = X_copy['Resting_BP(mm HG)'],
    color = 'darkgreen'
    )

ax.axvline(
    mean, 
    color = 'lightblue', 
    linestyle = 'dashed',
    label = f'Mean: {mean: .2f}'
    )

plt.legend()

plt.show()

"""
Slight skew to the right, no outliers on the lower end
"""

"""
9 outliers, saving for now
"""

restingBP_outliers = X_copy[X_copy['Resting_BP(mm HG)'] > upper_bound]['Resting_BP(mm HG)']


# Cholesterol

basic_stats = X_copy['Cholesterol(mg/dl)'].describe()

mean = X_copy['Cholesterol(mg/dl)'].mean()

IQR = basic_stats['75%'] - basic_stats['25%']

upper_bound = basic_stats['75%'] + 1.5*IQR
lower_bound = basic_stats['25%'] - 1.5*IQR

"""
Box plot
"""

ax = sns.boxplot(
    x = X_copy['Cholesterol(mg/dl)'],
    color = 'darkgreen'
    )

ax.axvline(
    mean, 
    color = 'lightblue', 
    linestyle = 'dashed',
    label = f'Mean: {mean: .2f}'
    )

plt.legend()

plt.show()

"""
5 outliers, saving for later
"""

choles_outliers = X_copy[X_copy['Cholesterol(mg/dl)'] > upper_bound]['Cholesterol(mg/dl)']


# Fasting Blood sugar

X_copy['Fasting_Blood_Sugar(> 120 mg/dl)'].value_counts()

X_copy['Fasting_Blood_Sugar(> 120 mg/dl)'] = X_copy['Fasting_Blood_Sugar(> 120 mg/dl)'].astype('category')

"""
Plotting bar plot
"""

plt.figure(figsize = (10, 6))
ax = sns.countplot(x = X_copy['Fasting_Blood_Sugar(> 120 mg/dl)'])

ax.set_xticklabels(['False', 'True'])
plt.xlabel('Is Fasting Blood Sugar Above 120 mg/dl?')

plt.show()


# Resting ECG Results

X_copy['Resting_ECG_Results'].value_counts()

X_copy['Resting_ECG_Results'] = X_copy['Resting_ECG_Results'].astype('category')

"""
Plotting bar plot
"""

plt.figure(figsize = (10, 6))
ax = sns.countplot(x = X_copy['Resting_ECG_Results'])

for bar in ax.patches:
    bar_height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar_height + 0.1,
        f'{int(bar_height)}', 
        ha='center', 
        va='bottom'    
    )

ax.set_xticklabels(['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
plt.xlabel('Results of ECG', labelpad = 20)

plt.show()