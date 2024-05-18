import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('Datasets/PETR4 Dados Históricos.csv', sep=',')
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)

fig = go.Figure(data = go.Candlestick(
    x = df['Data'],
    open = df['Abertura'],
    high = df['Máxima'],
    low = df['Mínima'],
    close = df['Último']
))

fig.show()