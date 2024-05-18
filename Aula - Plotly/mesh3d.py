import plotly.graph_objects as go
import numpy as np

N = 70
x = 70 * np.random.randn(N)
y = 60 * np.random.randn(N)
z = 50 * np.random.randn(N)

fig = go.Figure(data = go.Mesh3d(x = x, y = y, z = z, opacity = 0.5))

fig.show()