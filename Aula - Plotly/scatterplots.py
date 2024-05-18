import plotly.graph_objects as go
import numpy as np

t = np.linspace(0, 10, 100)
y = np.sin(t)

fig = go.Figure(data=go.Scatter(x=t, y=y, mode='markers+lines'))

fig.show()

n = 100
x = np.linspace(0, 1, n)
x1 = np.random.randn(n)

y0 = x1 + 5
y1 = x1
y2 = x1 - 5

fig = go.Figure()

fig.add_traces(go.Scatter(x=x, y=y0, mode='markers', name='markers'))
fig.add_traces(go.Scatter(x=x, y=y1, mode='lines+markers', name='lines+markers'))
fig.add_traces(go.Scatter(x=x, y=y2, mode='lines', name='lines'))

fig.show()

x = [1, 2, 3, 4]
y = [10, 11, 12, 13]
mdict = dict(size=[40, 60, 80, 100], color=[0, 1, 2, 3])

fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker=mdict, hovertemplate="R$ %{y} - %{marker.size}"))

fig.show()