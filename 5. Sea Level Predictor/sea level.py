import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
 df=pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
 df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level',color='red',label='Original Data')


 # Create first line of best fit
 x=df['Year']
 y=df['CSIRO Adjusted Sea Level']
 # Calculating intercept and slop using scipy.stats.linregress() for first line of best fit
 result = linregress(x, y)
 slope=result.slope
 intercept=result.intercept
 print(slope, intercept)
 plt.plot(range(1880, 2051, 1), slope * range(1880, 2051, 1) + intercept,label='extended fitted line (1880-2050)')
 #plt.show()
 y_pred = [slope * xi + intercept for xi in range(1880, 2051, 1)]
 print(y_pred[-1])
# Create second line of best fit
#Subsetting dataframe to year >=2000
 df2=df.loc[(df['Year']>=2000)]
 x2=df2['Year']
 y2=df2['CSIRO Adjusted Sea Level']
 result2= linregress(x2, y2)
 slope2=result2.slope
 intercept2=result2.intercept
 fig=plt.plot(range(2000, 2051, 1), slope2 * range(2000, 2051, 1) + intercept2, 'k',label='extended fitted line adjusted (2000-2050)')
 y_pred2 = [slope2 * xi + intercept2 for xi in range(2000, 2051, 1)]
 print(y_pred2[-1])
 plt.legend()
# Add labels and title
 plt.title('Rise in Sea Level')
 plt.xlabel('Year')
 plt.ylabel('Sea Level (inches)')

 #plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
 plt.savefig('sea_level_plot.png')
 return plt.gca()
draw_plot()
