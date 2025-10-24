 # Matplotlib/Seaborn charts
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import our data files
df = pd.read_csv('../data/USvideos.csv')
df_cat = pd.read_json('../data/US_category_id.json')

# Heatmap of numerica data
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('YouTube Numerical Statistics Correlations')
plt.show()