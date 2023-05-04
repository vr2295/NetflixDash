from dash import html
import dash
import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
from app import app
server = app.server
nf = pd.read_csv(r'Best Movies Netflix.csv')
df1 = nf.groupby(['RELEASE_YEAR'])[['SCORE','NUMBER_OF_VOTES']].mean()
df2 = nf.groupby(['MAIN_GENRE'])[['SCORE','NUMBER_OF_VOTES']].mean()

fig1 = px.scatter(df1, x='NUMBER_OF_VOTES', y='SCORE')

header = html.H3('KPI: SCORE and VOTES')
dd_opt = ['SCORE','NUMBER_OF_VOTES']
layout = html.Div([
        header,
        dbc.Container([
            dbc.Row([
                html.Div([
                    html.Div([
                    html.Label('Select Country/Countries'),
                    dcc.Dropdown(id='dropdown',
                            options=dd_opt,
                            value='SCORE')
                    ],style={'width': '49%', 'display': 'inline-block'})
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    html.H4("Scatter Plot Between Score and Number of Votes"),
                    dcc.Graph(id="graph1", figure=fig1)
                ], width=6),
                dbc.Col([
                    html.H4("Average Score and No. of Votes For Each Major Genre"),
                    dcc.Graph(id="graph2")
                ], width=6)
            ])
        ])
])

@app.callback(
        Output("graph2", "figure"),
        Input("dropdown", "value"))
def generate_chart(column):
    if not column:
        dash.no_update
    fig2 = px.bar(df2, x=df2.index, y=column)
    return(fig2)
