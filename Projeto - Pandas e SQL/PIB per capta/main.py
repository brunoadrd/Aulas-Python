import pandas as pd
import numpy as np

df_gdp = pd.read_csv('Datasets/gdp.csv', decimal='.')

df_gdp['Year'] = pd.to_datetime(df_gdp['Year'])
df_gdp['Year'] = df_gdp['Year'].apply(lambda x: int(x.year))

df_gdp.rename(columns={' GDP_pp ': 'GDP_pp'}, inplace=True)

df_gdp['GDP_pp'] = df_gdp['GDP_pp'].str.replace(' ', '')
df_gdp['GDP_pp'] = df_gdp['GDP_pp'].str.replace(",", "").astype(float)

df_gdp.groupby('Country')['Year'].min()

#print(
#    df_gdp.groupby('Country')['Year'].min()[
#        df_gdp.groupby('Country')['Year'].min() == df_gdp.groupby('Country')['Year'].min().max()
#    ]
#)

lower_year = df_gdp[df_gdp['Year'] < 2000].min()['Year']
higher_year = df_gdp[df_gdp['Year'] < 2000].max()['Year']

df_gdp_start = df_gdp[df_gdp['Year'] == lower_year].groupby('Region')['GDP_pp'].mean()
df_gdp_end = df_gdp[df_gdp['Year'] == higher_year].groupby('Region')['GDP_pp'].mean()

#print(((df_gdp_end - df_gdp_start) / df_gdp_start * 100).sort_values())

arr_year = np.arange(df_gdp['Year'].min(), df_gdp['Year'].max())
df_all_years = pd.DataFrame(arr_year, columns=['Year'])
df_all_years.index = df_all_years['Year']

df_years_off = ~df_all_years['Year'].isin(df_gdp['Year'])
df_years_off = df_all_years.loc[df_years_off].index

df_gdp = df_gdp.sort_values(['Country', 'Year'])

df_gdp['delta_gdp'] = df_gdp['GDP_pp'] - df_gdp['GDP_pp'].shift(1)
df_gdp['delta_year'] = df_gdp['Year'] - df_gdp['Year'].shift(1)
df_gdp['gdp_year'] = (df_gdp['delta_gdp'] / df_gdp['delta_year']).shift(-1)

df_gdp['next_year'] = df_gdp['Year'].shift(-1)
del df_gdp['delta_gdp'], df_gdp['delta_year']

df_new_data = pd.DataFrame()

for idx, row in df_gdp.iterrows():
    if row['Year'] == 2011:
        continue

    years_to_add = df_years_off[(df_years_off < row['next_year']) & (df_years_off > row['Year'])]

    for new_year in years_to_add:
        add_row = row.copy()
        add_row['GDP_pp'] = (new_year - add_row['Year']) * add_row['gdp_year'] + add_row['GDP_pp']
        add_row['Year'] = new_year
        add_row['kind'] = 'estimated'
        df_new_data = pd.concat([df_new_data, add_row.to_frame().transpose()])

df_gdp = pd.concat([df_gdp, df_new_data])
df_gdp = df_gdp.sort_values(['Country', 'Year'])
df_gdp.index = df_gdp['Year']
df_gdp['kind'] = df_gdp['kind'].fillna('real')

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(20,5))

country = 'Brazil'
df_gdp[(df_gdp['kind'] == 'real') & (df_gdp['Country'] == country)].plot(kind='scatter', y='GDP_pp', x='Year', ax=ax)
df_gdp[(df_gdp['kind'] == 'estimated') & (df_gdp['Country'] == country)].plot(kind='scatter', y='GDP_pp', x='Year', ax=ax, color='orange')