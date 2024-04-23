import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the data
df = pd.read_csv('Best Games Steam.csv')

# Data Cleaning
# Converting rating percentages to float
df['Rating'] = df['Rating'].str.replace('%', '').astype(float)
# Converting price to numeric, setting errors='coerce' will convert non-numeric values to NaN
df['Price'] = pd.to_numeric(df['Price'].str.replace('$', ''), errors='coerce')

# Calculate basic statistics
statistics = df.describe()

# Display statistics
print("Basic Statistics:")
print(statistics)

# Data Visualization
plt.figure(figsize=(10, 6))

# Rating Distribution Plot
plt.subplot(1, 2, 1)
sns.histplot(df['Rating'], kde=True)
plt.title('Rating Distribution')
plt.xlabel('Rating (%)')
plt.ylabel('Frequency')

# Price Distribution Plot
plt.subplot(1, 2, 2)
sns.histplot(df['Price'].dropna(), kde=True)  # Drop NaN values for price
plt.title('Price Distribution')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Scatter Plot of Rating vs. Price
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Rating', y='Price', data=df)
plt.title('Rating vs. Price')
plt.xlabel('Rating (%)')
plt.ylabel('Price ($)')
plt.grid(True)
plt.show()
