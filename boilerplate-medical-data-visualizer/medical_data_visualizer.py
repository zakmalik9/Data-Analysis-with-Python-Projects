import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
weight = df['weight']
height = df['height'] / 100
bmi = weight / (height ** 2)
mask = bmi > 25

df['overweight'] = 0
df.loc[mask, 'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
chol = df['cholesterol']
gluc = df['gluc']
mask1 = chol > 1
mask2 = gluc > 1

df['cholesterol'] = 0
df['gluc'] = 0
df.loc[mask1, 'cholesterol'] = 1
df.loc[mask2, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df[['cardio', 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']]
    df_cat = df_cat.melt(id_vars='cardio')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    totals = df_cat.groupby(['cardio', 'variable']).value_counts(sort=False)

    df_cat = totals.index.to_frame(index=False)
    df_cat['total'] = totals.values

    # Draw the catplot with 'sns.catplot()'
    facetgrid = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)
    fig = facetgrid.fig
    plt.show()

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_hi'] >= df['ap_lo']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt='.1f', vmax=0.3, vmin=-0.14, center=0, linewidth=0.5, mask=mask, ax=ax, cbar_kws={'shrink': 0.5, 'ticks': [-0.08, 0.00, 0.08, 0.16, 0.24]})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
