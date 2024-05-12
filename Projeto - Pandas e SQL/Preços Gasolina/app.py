import pandas as pd

df1 = pd.read_csv('datasets/gasolina_2000+.csv', index_col=0)
df2 = pd.read_csv('datasets/gasolina_2010+.csv', index_col=0)

df = pd.concat([df1, df2])

df['DATA INICIAL'] = pd.to_datetime(df['DATA INICIAL'])
df['DATA FINAL'] = pd.to_datetime(df['DATA FINAL'])

df['ANO-MES'] = df['DATA FINAL'].apply(lambda x: '{}-{:02d}'.format(x.year, x.month))

df_comumgas = df[df['PRODUTO'] == 'GASOLINA COMUM']

print(df_comumgas[df_comumgas['ANO-MES'] == '2008-08']['PREÇO MÉDIO REVENDA'].mean())
print(df_comumgas[(df_comumgas['ANO-MES'] == '2014-05') & (df_comumgas['ESTADO'] == 'SAO PAULO')]['PREÇO MÉDIO REVENDA'].mean())

print(df_comumgas[df_comumgas['PREÇO MÉDIO REVENDA'] > 5][['ANO-MES', 'ESTADO', 'PREÇO MÉDIO REVENDA']])

df_filtroano = df_comumgas[df_comumgas['DATA FINAL'].apply(lambda x: x.year == 2012)]

print(df_filtroano[df_filtroano['REGIÃO'] == 'SUL']['PREÇO MÉDIO REVENDA'].mean())

df_comumgas['MES'] = df_comumgas['DATA FINAL'].apply(lambda x: x.month)
df_rio = df_comumgas[df_comumgas['ESTADO'] == "RIO DE JANEIRO"]

df_mes_rio = df_rio.groupby('ANO-MES')[['PREÇO MÉDIO REVENDA', 'MES']].last()
(df_mes_rio[df_mes_rio['MES'] == 12]['PREÇO MÉDIO REVENDA'] / df_mes_rio[df_mes_rio['MES'] == 12]['PREÇO MÉDIO REVENDA'].shift(1) - 1) * 100

print((df_mes_rio[df_mes_rio['MES'] == 12] / df_mes_rio[df_mes_rio['MES'] == 12].shift(1) - 1) * 100)

df_serietemporal = pd.DataFrame()

df_max = df_comumgas.groupby('ANO-MES')['PREÇO MÉDIO REVENDA'].max()
df_min = df_comumgas.groupby('ANO-MES')['PREÇO MÉDIO REVENDA'].min()

df_serietemporal['MIN'] = df_min
df_serietemporal['MAX'] = df_max
df_serietemporal['DIF ABSOL'] = df_max - df_min
df_serietemporal['DIF %'] = ((df_max - df_min) / df_min) * 100

indice_max = df_comumgas.groupby('ANO-MES')['PREÇO MÉDIO REVENDA'].idxmax()
indice_min = df_comumgas.groupby('ANO-MES')['PREÇO MÉDIO REVENDA'].idxmin()

df_serietemporal['ESTADO MIN'] = df_comumgas.loc[indice_min, :]['ESTADO'].values
df_serietemporal['ESTADO MAX'] = df_comumgas.loc[indice_max, :]['ESTADO'].values

print(df_serietemporal)