import dash
import dash_bootstrap_components as dbc

from psycoviddash.functions import *

# THIS THING MAKES THE JOBLIB WORK WITH FLASK APPS DEPLOYMENT
import __main__

__main__.edu_func = edu_func
__main__.edu_mom_func = edu_mom_func
__main__.risk_group_func = risk_group_func
__main__.expat_func = expat_func
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

app.title = "PsyCovid Project"

server = app.server