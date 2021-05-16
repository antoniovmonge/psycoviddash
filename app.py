import dash
import dash_bootstrap_components as dbc
import pandas as pd
# from flask_caching import Cache

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name':'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}],
                external_stylesheets=[dbc.themes.MINTY]
                )
# cache = Cache(app.server, config={
#     'CACHE_TYPE': 'redis',
#     # Note that filesystem cache doesn't work on systems with ephemeral
#     # filesystems like Heroku.
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_DIR': 'cache-directory',

#     # should be equal to maximum number of users on the app at a single time
#     # higher numbers will store more data in the filesystem / redis cache
#     'CACHE_THRESHOLD': 200
# })

# def get_dataframe():
#     @cache.memoize()
#     def get_data():
#         return pd.read_csv("s3://psycovid/cleaned_data_040321.csv", index_col=0)

server = app.server