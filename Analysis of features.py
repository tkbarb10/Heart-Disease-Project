# === Univariate Analysis ===

# Start with Age

mean = X['age'].mean()
median = X['age'].median()

"""
Plotting histogram with basic stats
"""

plt.figure(figsize = (10,6))

ax = sns.histplot(X['age'], edgecolor = 'black')

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

X_copy['sex'] = X_copy['sex'].astype('category')

plt.figure(figsize = (10, 6))

ax = sns.barplot(X_copy['sex'], color = 'red', alpha = .7)
ax.set_yticklabels([label.get_text().title() for label in ax.get_yticklabels()])

plt.show()

# Chest Pain

new_values = {1: 'Typical', 2: 'Atypical', 3: "Non-Anginal", 4: 'Asymptomatic'}

X_copy['cp'] = X_copy['cp'].map(new_values)

sorted_order = X_copy['cp'].value_counts().index


plt.figure(figsize = (12, 6))

ax = sns.countplot(x = 'cp', data = X_copy, order = sorted_order)

ax.set_ylabel('Count')
ax.set_xlabel('Chest Pain Type')

plt.show()


