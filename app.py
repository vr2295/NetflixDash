import dash
import dash_bootstrap_components as dbc
server = app.server
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.QUARTZ])
