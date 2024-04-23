import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the data
df = pd.read_csv('Best Games Steam.csv')

df['Rating'] = df['Rating'].str.replace('%', '').astype(float)
df['Price'] = pd.to_numeric(df['Price'].str.replace('$', ''), errors='coerce')

# Drop rows where price is NaN
df = df.dropna(subset=['Price'])

# Adjust the number of colors based on the number of unique years
unique_years = df['Year'].nunique()
palette = sns.cubehelix_palette(start=2.8, rot=.1, light=0.8, dark=0.2, n_colors=unique_years)

# Visualization with seaborn
plt.figure(figsize=(12, 8))
scatter = sns.scatterplot(x='Rating', y='Price', hue='Year', size='Price',
                          sizes=(40, 400), alpha=0.7, palette=palette, data=df)
plt.title('Rating vs. Price Colored by Year', fontsize=16)
plt.xlabel('Rating (%)', fontsize=14)
plt.ylabel('Price ($)', fontsize=14)
plt.grid(True)

# Add a regression line to show the trend
sns.regplot(x='Rating', y='Price', data=df, scatter=False, color='black', ci=None)

# Creating a legend manually if legend_elements is not available
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()
