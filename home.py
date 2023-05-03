from dash import html
import dash_bootstrap_components as dbc
import dash

header = html.H3('Welcome to the Home page!')

layout = html.Div([
        header,
        html.Div([
            dbc.Container([
                dbc.Row([
                dbc.Col(html.H1("Netflix Movies Dashboard", className="text-center")
                    , className="mb-5 mt-5")
                ]),
            dbc.Row([
                dbc.Col(html.H5(children='FILL THE INFORMATION HERE '
                        ), className="mb-4")
            ]),

            dbc.Row([
                dbc.Col(html.H5(children='FILL THE INFORMATION HERE'
                        ), className="mb-5")
        ]),
            dbc.Row([
                dbc.Col(dbc.Card(children=[html.H5(children='Netflix Inc. is an American media company based in Los Gatos, California. Founded in 1997 by Reed Hastings and Marc Randolph in Scotts Valley, California, it operates the over-the-top subscription video on-demand service Netflix brand, which includes original films and television series commissioned or acquired by the company, and third-party content licensed from other distributors.',
                                               className="text-left"),
                                                dbc.Button("Netflix Wikipedia",
                                                href="https://en.wikipedia.org/wiki/Netflix",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-4"),

                dbc.Col(dbc.Card(children=[html.H3(children='Link to the GitHub page of the Project',
                                               className="text-center"),
                                       dbc.Button("GitHub",
                                                  href="https://github.com/JackLinusMcDonnell/DashAppTeaching",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-4"),

            ], className="mb-5"),

        ])
    ])
])
