import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
#print(df.head())
df.set_index(df['date'])
df['date']=pd.to_datetime(df['date'])
#print(df['value'].count())



# Clean data
#Calculate values to drop
drop_value=int(round(2.5/100*df['value'].count(),0))
#print(drop_value)

index_val1=df.nlargest(drop_value, 'value').index

df.drop(index_val1, inplace=True)
index_val2=df.nsmallest(drop_value, 'value').index
#dropping top and bottom values
df.drop(index_val2, inplace=True)
df_bar = df.copy()
df_box = df.copy()
def draw_line_plot():
    # Draw line plot
 fig=plt.figure()
 plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
 plt.xlabel('Date')
 plt.ylabel('Page Views')
 plt.plot(df['date'], df['value'])


 #plt.show()


    # Save image and return fig (don't change this part)
 fig.savefig('line_plot.png')
 return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
# df_bar = df.copy()
 #df_bar.reset_index(inplace=True)
 df_bar['month2']=pd.to_datetime(df_bar['date']).dt.month
 df_bar['year'] = [d.year for d in df_bar.date]
 df_bar['Months'] = [d.strftime('%B') for d in  df_bar.date]
 #df_bar.set_index('year')
 #grouping data by year and average mont page views
 group=pd.DataFrame(df_bar['value'].groupby([df_bar['year'],df_bar['month2'],df_bar['Months']]).mean())
 #group is a pd.Series type. Must be transformed into a DataFrame
 #group_df=pd.DataFrame(group)
 #plotting the results
 #width = 0.25  # the width of the bars
 #multiplier = 0
 fig, ax = plt.subplots(layout='constrained')
 #plt.bar(x=group_df['year'])
 sns.barplot(data=group,x='year',y='value',hue='Months',hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], dodge='auto')
 #['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],dodge='auto')
 plt.xlabel('Years')
 plt.ylabel('Average Page Views')
 plt.xticks(rotation=45)
 #plt.show()
    # Save image and return fig (don't change this part)
 fig.savefig('bar_plot.png')
 plt.close()
 return fig

def draw_box_plot():
    # Prepare data for box plots       (this part is done!)
 df_box = df.copy()
 df_box.reset_index(inplace=True)
 df_box['date']=pd.to_datetime(df_box['date'])
 df_box['month2']=pd.to_datetime(df_box['date']).dt.month
 df_box['year'] = [d.year for d in     df_box.date]
 df_box['month'] = [d.strftime('%b') for d in  df_box.date]
 #sort dataframe by month number, to display months and values in  the correct order
 df2=df_box.sort_values(by='month2')
    # Draw box plots (using Seaborn)

 fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))
 sns.boxplot(x=df_box['year'],  y=df_box['value'], hue=df_box['year'], legend=False, ax=ax[0])
 ax[0].set_title('Year-wise Box Plot (Trend)', fontsize=18, loc='center')
 ax[0].set_xlabel('Year')
 ax[0].set_ylabel('Page Views')
 sns.boxplot(x=df2['month'], y=df2['value'], hue=df2['month'], ax=ax[1])
 ax[1].set_title('Month-wise Box Plot (Seasonality)' , fontsize=18)
 ax[1].set_xlabel('Month')
 ax[1].set_ylabel('Page Views')
 #plt.show()
    # Save image and return fig (don't change this part)
 fig.savefig('box_plot.png')
 return fig


draw_line_plot()
draw_bar_plot()
draw_box_plot()

