import pandas as pd
import numpy as np

df_obesity = pd.read_csv('Datasets/obesity_cleaned.csv')

#print(df_obesity['Obesity (%)'].value_counts())

del df_obesity['Unnamed: 0']

df_obesity['Obesity'] = df_obesity['Obesity (%)'].str.split(expand=True)[0]

df_obesity.loc[df_obesity['Obesity'] == 'No', 'Obesity'] = np.nan

df_obesity['Obesity'] = df_obesity['Obesity'].astype(float)

#print(df_obesity[df_obesity['Year'] == 2015].groupby('Sex').mean(numeric_only=True).drop('Year', axis=1))

lower_year = df_obesity['Year'].min()
higher_year = df_obesity['Year'].max()

df_start = df_obesity[df_obesity['Year'] == lower_year]
df_end = df_obesity[df_obesity['Year'] == higher_year]

df_start = df_start[df_start['Sex'] == 'Both sexes']
df_end = df_end[df_end['Sex'] == 'Both sexes']

df_start.set_index('Country', inplace=True)
df_end.set_index('Country', inplace=True)

#print((df_end['Obesity'] - df_start['Obesity']).sort_values().head(5))
#print((df_end['Obesity'] - df_start['Obesity']).sort_values(ascending=0).head(5))

#print(df_obesity[df_obesity['Year'] == 2015].set_index('Country').sort_values(by=['Obesity'], ascending=0).head(1))
#print(df_obesity[df_obesity['Year'] == 2015].set_index('Country').sort_values(by=['Obesity'], ascending=1).head(1))

df_brazil = df_obesity[df_obesity['Country'] == 'Brazil'].set_index('Year').drop('Country', axis=1)

#print(df_brazil[df_brazil['Sex'] == 'Female']['Obesity'] - df_brazil[df_brazil['Sex'] == 'Male']['Obesity'])

#(df_brazil[df_brazil['Sex'] == 'Female']['Obesity'] - df_brazil[df_brazil['Sex'] == 'Male']['Obesity']).plot()

df_world = df_obesity.set_index('Year')

print(df_world[df_world['Sex'] == 'Both sexes'].groupby('Year')['Obesity'].mean())

(df_world[df_world['Sex'] == 'Both sexes'].groupby('Year')['Obesity'].mean()).plot()