import plotly.graph_objects as go

animais = ['Girafas', 'Macacos', 'Tigres']

fig = go.Figure(
    data = [
        go.Bar(x=animais, y=[3, 40, 6], name='Zoológico SP'),
        go.Bar(x=animais, y=[1, 20, 3], name='Zoológico RS')
    ]
)

fig.update_layout(barmode='stack')

fig.show()

colors = ['lightslategray'] *5
colors[1] = 'blue'

fig = go.Figure(
    data = go.Bar(
        x = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E'],
        y = [20, 14, 23, 25, 22],
        marker_color = colors
    )
)

fig.show()