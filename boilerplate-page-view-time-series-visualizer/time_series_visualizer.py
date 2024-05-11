import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    fig, ax = plt.subplots(figsize=(32, 10))
    ax.plot(df, c='#CE2029', linewidth=3)
    
    ax.set_xlabel('Date', fontsize=20)
    plt.xticks(fontsize=20)
    
    ax.set_ylabel('Page Views', fontsize=20)
    plt.yticks(fontsize=20)
    
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=24)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month

    totals = df_bar.groupby(['Years', 'Months'], sort=False).mean()
    df_bar = totals.index.to_frame(index=False)
    df_bar['Average Page Views'] = totals.values
  
    # Draw bar plot
    g = sns.catplot(x='Years', y='Average Page Views', hue='Months', kind='bar', palette=sns.color_palette(), data=df_bar, legend_out=False)
    
    labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for t, l in zip(g._legend.texts, labels):
      t.set_text(l)
    g.set_xticklabels(rotation=90, fontsize=8.8)
    
    fig = g.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2)= plt.subplots(figsize=(28.8, 10.3), ncols=2)
    ylimit = 200000
    yticks = [0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]
    
    ax1 = sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylim(top=ylimit)
    ax1.set_yticks(yticks)
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')
    
    labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax2 = sns.boxplot(x='month', y='value', data=df_box, hue_order=labels, ax=ax2, order=labels)
    ax2.set_xlabel('Month')
    ax2.set_ylim(top=ylimit)
    ax2.set_yticks(yticks)
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
