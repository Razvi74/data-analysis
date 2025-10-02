import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
#Using an intermediate column ['bmi'] to calculate body mass index
df['bmi']=df['weight']/(df['height']/100*df['height']/100)
df['overweight'] = df['bmi'].apply(lambda x: 1 if x >= 25 else 0)
#Dropping the intermediate column
df.drop(['bmi'],axis=1,inplace=True)


# 3
df['gluc'] = df['gluc'].apply(lambda x: 0 if x ==1 else 1)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x ==1 else 1)
print(df)

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                     value_name='value')

    # 6
    df_cat['total'] = 1

    # 7
    g = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
    # The resulting dataframe is in long format.
    # 8
    fig=sns.catplot(x="variable",y="total",data=g,hue="value",kind="bar",col="cardio")

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    #Define conditions for filtering
    cond1 = (df['ap_lo'] <= df['ap_hi'])
    cond2 = (df['height'] >= df['height'].quantile(0.025))
    cond3 = (df['height'] <= df['height'].quantile(0.975))
    cond4 = (df['weight'] >= df['weight'].quantile(0.025))
    cond5 = (df['weight'] <= df['weight'].quantile(0.975))
    #Filter the data
    df_heat = df.loc[cond1 & cond2 & cond3 & cond4 & cond5]
    #Rename columns according to example heatmap
    #df_heat.columns = ['id', 'age', 'height', 'gender', 'height', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke',
     #                  'alco', 'active', 'cardio', 'overweight']

    # 12 Calculate the correlation matrix
    corr=df_heat.corr()
    print(corr)

    # 13 Generate a mask for the upper triangle and store it
    mask = np.triu(corr)

    # 14 Setup matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15 Plot the correlation matrix
    sns.heatmap(corr, linewidths=1, annot=True, square=True, mask=mask, fmt=".1f", center=0.08,
                cbar_kws={"shrink": 0.5})

    # 16
    fig.savefig('heatmap.png')
    return fig
draw_heat_map()
draw_cat_plot()
