import plotly.graph_objects as go

labels = ['Oxigênio', 'Hidrogênio', 'Gás Carbônico', 'Nitrogênio']
values = [4500, 2500, 1060, 500]
colors = dict(colors=['green', '#FF0041', 'blue', 'pink'])

fig = go.Figure(
    data = go.Pie (
        labels = labels,
        values = values,
        pull = [0, 0, 0.3, 0]
    )
)

fig.update_traces(hoverinfo='label+percent', textinfo='value+percent', textfont_size = 15, marker=colors)

fig.show()