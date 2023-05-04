from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import home
import page_2
import page_3
from app import app

app.config.suppress_callback_exceptions = True

navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Page 2", href='/page-2'),
                    dbc.DropdownMenuItem("Page 3", href='/page-3'),
                ],
            ),
        ],
        brand="Netflix",
        brand_href="/",
        sticky="top",
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-2':
        return page_2.layout
    if pathname == '/page-3':
        return page_3.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=False)
