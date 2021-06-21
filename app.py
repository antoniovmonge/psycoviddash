import dash
import dash_bootstrap_components as dbc

# from functions import *
# import pandas as pd
# from flask_caching import Cache

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    meta_tags=[
        {
            'name':'viewport',
            'content': 'width=device-width, initial-scale=1.0'
        }
    ],
    # external_stylesheets=external_stylesheets
    external_stylesheets=[dbc.themes.MINTY]
)


server = app.server