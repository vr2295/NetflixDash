from dash import html
import dash
import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
from app import app
from plotly.subplots import make_subplots
server = app.server
header = html.H3('Major Genre & Main Production')
nf = pd.read_csv(r'Best Movies Netflix.csv')
df3 = pd.DataFrame(nf.groupby(['MAIN_PRODUCTION','MAIN_GENRE'])[['DURATION','SCORE']].mean())
df3 = df3.reset_index()

df4 = pd.DataFrame(nf['MAIN_GENRE'].value_counts())
df4 = df4.reset_index()

mp = [{'label': val, 'value': val} for val in df3['MAIN_PRODUCTION'].unique()]
mg = [{'label': genre, 'value': genre} for genre in df4['index'].unique()]

layout = html.Div([
        header,
        dbc.Container([
            dbc.Row([
                html.Div([
                    html.Div([
                    html.Label('Select Production'),
                    dcc.Dropdown(id='prod_dd',
                            options=mp,
                            value=['IN','US','JP','GB'],
                            multi=True)
                    ],style={'width': '49%', 'display': 'inline-block'})
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    html.H4("Duration and Score Combo Plot"),
                    dcc.Graph(id="graph3")
                ])
            ]),
            dbc.Row([
                html.Div([
                    html.Div([
                    html.Label('Select Genre'),
                    dcc.Dropdown(id='genre_dd',
                            options=mg,
                            value=['drama','thriller'],
                            multi=True)
                    ],style={'width': '49%', 'display': 'inline-block'})
                ]),
            dbc.Row([
                dbc.Col([
                    html.H4("Pie Chart"),
                    dcc.Graph(id="graph4")
                ])
            ])
        ])
])
])

@app.callback(
        Output("graph3", "figure"),
        Input("prod_dd", "value"))

def generate_chart(prod):
    if not prod:
        dash.no_update

    mask = df3.MAIN_PRODUCTION.isin(prod)
    fig3 = make_subplots(specs=[[{"secondary_y": True}]])
    fig3.add_trace(go.Line(x=df3[mask]['MAIN_PRODUCTION'], y=df3['SCORE']), secondary_y=True)
    fig3.add_trace(go.Bar(x=df3[mask]['MAIN_PRODUCTION'], y=df3['DURATION']), secondary_y=False)
    return(fig3)

@app.callback(
        Output("graph4", "figure"),
        Input("genre_dd", "value"))
def generate_chart(genre):
    if not genre:
        dash.no_update
    mask1 = df4['index'].isin(genre)
    fig4 = px.pie(df4[mask1], values='MAIN_GENRE', names='index', title='Count of the Major Genres')
    return(fig4)
