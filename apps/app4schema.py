import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from app import app

fig = go.Figure()


layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.H1(
                'Project Schema',
                className='text-center'),
            html.Br(),
            html.Br(),
            dbc.Col(
                    
                        html.Img(
                            src=app.get_asset_url("Psycovid_Schema.svg"),
                            className="logo",
                        ),
                        # width={'size': 10, 'offset': 1}
                        
            ),
            html.Br(),
            html.Br(),
            dbc.Row(
                        dbc.Col(
                            [
                                dcc.Markdown(
                                    '**GitHub Repo:** https://github.com/antoniovmonge/psycoviddash',
                                    className='text-center'),    
                            ],
                            style=dict(
                                    paddingBottom=150
                            )
                        )
            ),
        ]
    )    
)