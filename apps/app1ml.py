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
                    className='sidebar div-for-slider five columns',
                    children=[
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[0]),
                                dcc.Slider(
                                    id='slider-0',
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
                                html.Div(id='slider-output-container-0')
                            ]
                        ),
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
                            html.H5(children=bff15_labels[3]),
                                dcc.Slider(
                                    id='slider-3',
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
                                html.Div(id='slider-output-container-3')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[4]),
                                dcc.Slider(
                                    id='slider-4',
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
                                html.Div(id='slider-output-container-4')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[5]),
                                dcc.Slider(
                                    id='slider-5',
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
                                html.Div(id='slider-output-container-5')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[6]),
                                dcc.Slider(
                                    id='slider-6',
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
                                # html.Div(id='slider-output-container-6')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[7]),
                                dcc.Slider(
                                    id='slider-7',
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
                                # html.Div(id='slider-output-container-7')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[8]),
                                dcc.Slider(
                                    id='slider-8',
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
                                # html.Div(id='slider-output-container-8')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[9]),
                                dcc.Slider(
                                    id='slider-9',
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
                                # html.Div(id='slider-output-container-9')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[10]),
                                dcc.Slider(
                                    id='slider-10',
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
                                # html.Div(id='slider-output-container-10')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[11]),
                                dcc.Slider(
                                    id='slider-11',
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
                                # html.Div(id='slider-output-container-11')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[12]),
                                dcc.Slider(
                                    id='slider-12',
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
                                # html.Div(id='slider-output-container-12')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[13]),
                                dcc.Slider(
                                    id='slider-13',
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
                                # html.Div(id='slider-output-container-13')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[14]),
                                dcc.Slider(
                                    id='slider-14',
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
                                # html.Div(id='slider-output-container-14')
                            ]
                        ),
                        
                        # html.Div(
                        #     children=[
                        #         html.H5('Choose age:'),
                        #         dcc.Input(
                        #             id='age',
                        #             placeholder='Enter a value...',
                        #             type='number',
                        #             min=18,
                        #             max=70,
                        #             step=1,
                        #         )
                        #         # html.Div(id='slider-output-container-1')
                        #     ]
                        # ),
                        # html.Div(
                        #     children=[
                        #         html.H5(children=bff15_labels[2]),
                        #         dcc.Slider(
                        #             id='slider-2',
                        #             min=1,
                        #             max=6,
                        #             marks={
                        #                 1: '1',
                        #                 2: '2',
                        #                 3: '3',
                        #                 4: '4',
                        #                 5: '5',
                        #                 6: '6'
                        #             },
                        #             value=3
                        #         ),
                        #         html.Div(id='slider-output-container-2')
                        #     ]        
                        # ),
                    ]
                ),
#--------------------------------------------------------
# PERSONALITY CHART
                html.Div(
                    className='chart-container five columns',
                    children=[
                        html.H1('Hi'),
                        html.H3(id='personality-values'),
                        dcc.Graph(
                            id='personality-chart',
                            config={"displayModeBar": False},
                        )
                    ]
                )
            ]
        )
    ]
)

@app.callback(
    
        Output('personality-values', 'children'),
    [
        Input('slider-0', 'value'),
        Input('slider-1', 'value'),
        Input('slider-2', 'value'),
        Input('slider-3', 'value'),
        Input('slider-4', 'value'),
        Input('slider-5', 'value'),
        Input('slider-6', 'value'),
        Input('slider-7', 'value'),
        Input('slider-8', 'value'),
        Input('slider-9', 'value'),
        Input('slider-10', 'value'),
        Input('slider-11', 'value'),
        Input('slider-12', 'value'),
        Input('slider-13', 'value'),
        Input('slider-14', 'value'),
    
    ]
)

def update_output(
    value0, value1, value2, value3, value4, value5,
    value6, value7, value8, value9, value10, value11,
    value12,value13,value14):
    return f'{value0, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14}'

def update_chart(Country1, Country2):
    
    knn = joblib.load('models/knn.joblib')
    # pred = knn.predict(
    #     values.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]])
    # prediction = pd.DataFrame(pred)
    # prediction.columns = ['neu', 'ext', 'ope', 'agr', 'con']
    
    categories = ['Neuroticism', 'Openness', 'Extraversion',
                'Agreeableness', 'Conscientiousness', 'Neuroticism']

    radar_chart_figure = go.Figure()

    radar_chart_figure.add_trace(
        go.Scatterpolar(
            r=[
                df[df.Country == Country1].groupby('Country')['neu'].mean()[0],
                df[df.Country == Country1].groupby('Country')['ope'].mean()[0],
                df[df.Country == Country1].groupby('Country')['ext'].mean()[0],
                df[df.Country == Country1].groupby('Country')['agr'].mean()[0],
                df[df.Country == Country1].groupby('Country')['con'].mean()[0],
                df[df.Country == Country1].groupby('Country')['neu'].mean()[0],
            ],
            theta=categories,
            fill='toself',
            name=Country1,
            # line_color='rgb(249, 153, 153)'
        )
    )
    
    radar_chart_figure.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[2, 5],
            ),
            angularaxis=dict(
                rotation=90,
                direction='counterclockwise'
            )
        ),
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=1.4,
            xanchor="center",
            x=0.5,
            font=dict(
                # family="Gravitas One",
                size=18,
                # color="RebeccaPurple"
            )
        ),
        font=dict(
            # family="Gravitas One",
            # size=18,
            # color="RebeccaPurple"
        )
    )
    return radar_chart_figure