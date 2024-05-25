import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
from dash_bootstrap_templates import load_figure_template

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
load_figure_template('slate')
server = app.server

df_data = pd.read_csv('supermarket_sales.csv')
df_data['Date'] = pd.to_datetime(df_data['Date'])

app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H2('Projeto Dash', style={'font-size': '60px'}),
                html.Hr(),
                html.H5('Cidades:'),
                dcc.Checklist(df_data['City'].value_counts().index, df_data['City'].value_counts().index, id='check_city', inputStyle={'margin': '0 8px 6px 24px'}),
                html.H5('Variável de análise:', style={'margin-top': '24px'}),
                dcc.RadioItems(['gross income', 'Rating'], 'gross income', id='main_variable', inputStyle={'margin': '0 8px 6px 24px'})
            ], style={'height': '100vh', 'padding': '24px'})
        ], sm = 2),
        dbc.Col([
            dbc.Row([
                dbc.Col([dcc.Graph(id='city_fig')], sm = 4),
                dbc.Col([dcc.Graph(id='gender_fig')], sm = 4),
                dbc.Col([dcc.Graph(id='pay_fig')], sm = 4)
            ]),
            dbc.Row([dcc.Graph(id='income_per_date_fig')]),
            dbc.Row([dcc.Graph(id='income_per_product_fig')])
        ], sm = 10),
    ]),
])

@app.callback(
    [
        Output('city_fig', 'figure'),
        Output('pay_fig', 'figure'),
        Output('gender_fig', 'figure'),
        Output('income_per_product_fig', 'figure'),
        Output('income_per_date_fig', 'figure')
    ],
    [
        Input('check_city', 'value'),
        Input('main_variable', 'value')
    ] 
)
def render_graphs(cities, main_variable):
    operation = np.sum if main_variable == 'gross income' else np.mean

    df_filtered = df_data[df_data['City'].isin(cities)]
    df_cities = df_filtered.groupby('City')[main_variable].apply(operation).to_frame().reset_index()
    df_gender = df_filtered.groupby(['Gender', 'City'])[main_variable].apply(operation).to_frame().reset_index()
    df_payment = df_filtered.groupby('Payment')[main_variable].apply(operation).to_frame().reset_index()
    df_date_income = df_filtered.groupby('Date')[main_variable].apply(operation).to_frame().reset_index()
    df_product_income = df_filtered.groupby(['Product line', 'City'])[main_variable].apply(operation).to_frame().reset_index()

    fig_city = px.bar(df_cities, x='City', y=main_variable)
    fig_gender = px.bar(df_gender, x='Gender', y=main_variable, color='City', barmode='group')
    fig_payment = px.bar(df_payment, x=main_variable, y='Payment', orientation='h')
    fig_date_income = px.bar(df_date_income, x='Date', y=main_variable)
    fig_product_income = px.bar(df_product_income, x=main_variable, y='Product line', color='City', orientation='h', barmode='group')
    
    for fig in [fig_city, fig_gender, fig_payment, fig_date_income]:
        fig.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=200)

    fig_product_income.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=400)

    return fig_city, fig_payment, fig_gender, fig_product_income, fig_date_income

if __name__ == '__main__':
    app.run_server(debug=False)