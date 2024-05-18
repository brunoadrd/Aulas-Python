import plotly.graph_objects as go
import numpy as np

x1 = np.random.randn(500)
x2 = np.random.randn(500) + 1

fig = go.Figure()
fig.add_trace(go.Histogram(x = x1))
fig.add_trace(go.Histogram(x = x2))

fig.update_layout(barmode='overlay')
fig.update_traces(opacity=0.7)

fig.show()

np.random.seed(1)

y1 = np.random.randn(50) - 1
y2 = np.random.randn(50) + 1

fig = go.Figure()
fig.add_trace(go.Box(y = y1))
fig.add_trace(go.Box(y = y2))

fig.show()