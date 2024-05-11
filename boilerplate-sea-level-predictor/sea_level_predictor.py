import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    #print(df.info(), df.head())

    # Create scatter plot
    plt.figure()
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x=x, y=y, marker='x', color='red')
    
    # Create first line of best fit
    result = linregress(x=x, y=y)
    years_extended = range(1880, 2051)
    plt.plot(years_extended, result.slope * years_extended  + result.intercept, color='blue')
    
    # Create second line of best fit
    mask = df['Year'] >=2000
    x = df.loc[mask, 'Year']
    y = df.loc[mask, 'CSIRO Adjusted Sea Level']
    
    result = linregress(x=x, y=y)
    years_extended = range(2000, 2051)
    plt.plot(years_extended, result.slope * years_extended  + result.intercept, color='green')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()