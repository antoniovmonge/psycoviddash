import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64

import numpy as np
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px

from app import app

# url='s3://psycovid/cleaned_data_040321.csv'
# df = pd.read_csv(url ,index_col=0)
df = pd.read_csv('raw_data/cleaned_data_040321.csv')

def edu_func(X):
        X['Dem_edu'] = X['Dem_edu'].replace({'Uninformative response': 0, 'None': 1, 'Up to 6 years of school': 2, 'Up to 9 years of school': 3,
                                            'Up to 12 years of school': 4, 'Some College, short continuing education or equivalent': 5, 'College degree, bachelor, master': 6, 'PhD/Doctorate': 7})
        return X[['Dem_edu']]

def edu_mom_func(X):
    X['Dem_edu_mom'] = X['Dem_edu_mom'].replace({'Uninformative response': 0, 'None': 1, 'Up to 6 years of school': 2, 'Up to 9 years of school': 3,
                                                'Up to 12 years of school': 4, 'Some College or equivalent': 5, 'College degree': 6, 'PhD/Doctorate': 7})
    return X[['Dem_edu_mom']]

def edu_risk_group(X):
    X['Dem_riskgroup'] = X['Dem_riskgroup'].replace(
        {'No': 1, 'Not sure': 2, 'Yes': 3})
    return X[['Dem_riskgroup']]

def dem_expat_func(X):
    X['Dem_Expat'] = X['Dem_Expat'].replace({'no': 0, 'yes': 1})
    return X[['Dem_Expat']]

kwargs = {}

bff15_options = ['Strongly disagree', 'Disagree',
                    'Slightly disagree', 'Slightly agree', 'Agree', 'Strongly agree']

bff15_labels = ['... is often concerned',
                '... easily gets nervous',
                '... is good at staying cool in stressful situations',
                '... likes to chat',
                '... is extrovert and sociable',
                '... is socially reserved',
                '... gets a lot of new ideas',
                '... appreciates arts and aesthetics',
                '... has a vivid imagination and can think of things that do not yet exist',
                '... is sometimes impolite to others',
                '... is forgiving towards others',
                '... is kind and considerate towards almost everyone',
                '... is thorough and meticulous',
                '... is lazy',
                '... is effective when I do something']



layout = html.Div(
    
    className='container',
    children=[

        html.Div(
            className='main-container',
            children=[
                html.Div(
                    className='sidebar div-for-slider',
                    children=[
                        html.Div(
                            children=[
                                html.H5(bff15_labels[1]),
                                dcc.Slider(
                                    id='slider-1',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-1')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[2]),
                                dcc.Slider(
                                    id='slider-2',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-2')
                            ]
                        ),
                        html.Div(
                            children=[
                            html.H5(children=bff15_labels[1]),
                                dcc.Slider(
                                    id='slider-1',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-1')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[2]),
                                dcc.Slider(
                                    id='slider-2',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-2')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[1]),
                                dcc.Slider(
                                    id='slider-1',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-1')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[2]),
                                dcc.Slider(
                                    id='slider-2',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-2')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[1]),
                                dcc.Slider(
                                    id='slider-1',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-1')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[2]),
                                dcc.Slider(
                                    id='slider-2',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-2')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[1]),
                                dcc.Slider(
                                    id='slider-1',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-1')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[2]),
                                dcc.Slider(
                                    id='slider-2',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-2')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[1]),
                                dcc.Slider(
                                    id='slider-1',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-1')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[2]),
                                dcc.Slider(
                                    id='slider-2',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-2')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[1]),
                                dcc.Slider(
                                    id='slider-1',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-1')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[2]),
                                dcc.Slider(
                                    id='slider-2',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-2')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[1]),
                                dcc.Slider(
                                    id='slider-1',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-1')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[2]),
                                dcc.Slider(
                                    id='slider-2',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-2')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[1]),
                                dcc.Slider(
                                    id='slider-1',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-1')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[2]),
                                dcc.Slider(
                                    id='slider-2',
                                    min=1,
                                    max=6,
                                    marks={
                                        1: '1',
                                        2: '2',
                                        3: '3',
                                        4: '4',
                                        5: '5',
                                        6: '6'
                                    },
                                    value=3
                                ),
                                html.Div(id='slider-output-container-2')
                            ]        
                        ),
                    ]
                ),
                html.Div(
                    className='chart-container',
                    children=[
                        html.H1('Hi')
                    ]
                )
            ]
        )
    ]
)
