import dash
import plotly.express as px
import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

df = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
})

fig = px.bar(df, x = 'Fruit', y = 'Amount', color='City')

app.layout = html.Div([
        html.H1('Hello Dash', id = 'h1'),
        html.Div('Dash: um Framework para Python'),
        dcc.Graph(figure=fig, id='graph'),
        html.Div([
            html.Label('Dropdown'),
            dcc.Dropdown(
                id='dp-1',
                options=[
                    {'label': 'Rio Grande do Sul', 'value': 'RS'},
                    {'label': 'São Paulo', 'value': 'SP'},
                    {'label': 'Paraná', 'value': 'PR'}
                ], style={'margin-bottom': '25px'}
            ),

            html.Label('Checklist'),
            dcc.Checklist(
                id='cl-1',
                options=[
                    {'label': 'Rio Grande do Sul', 'value': 'RS'},
                    {'label': 'São Paulo', 'value': 'SP'},
                    {'label': 'Paraná', 'value': 'PR'}
                ], style={'margin-bottom': '25px'}
            ),

            html.Label('Text input'),
            dcc.Input(value='Digite...', type='text', style={'margin-left': '10px'}),

            html.Label('Slider'),
            dcc.Slider(
                min = 0,
                max = 9,
                marks = {i: str(i) for i in range(1, 6)},
                value = 5
            ),

            html.H6('Altere o valor abaixo:'),
            html.Div([
                'Entrada', dcc.Input(id='my-input', value='Valor inicial', type='text')
            ]),
            html.Br(),
            html.Div(id='my-output'),
        ])
    ],
    id='div1'
)

@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')],
)
def update_output_div(value):
    return 'Saída: {}'.format(value)

if __name__ == '__main__':
    app.run_server(debug = True)