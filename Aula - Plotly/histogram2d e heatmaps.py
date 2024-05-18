import plotly.graph_objects as go
import numpy as np

np.random.seed(1)

x = np.random.randn(500)
y = np.random.randn(500) + 1

fig = go.Figure(data = go.Histogram2d(x = x, y = y))

fig.show()

z = [[1, None, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]] # y[x]
x = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
y = ['Manhã', 'Tarde', 'Noite']

fig = go.Figure(data = go.Heatmap(z = z, x = x, y = y))

fig.show()