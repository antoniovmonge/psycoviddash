import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import dash_table
from dash_table.Format import Format, Scheme, Trim

import numpy as np
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
from joblib import load

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
    
    style=dict(
        paddingLeft=100,
        paddingRight=100,
    ),
    children=[
        html.Div(
            className='main-container',
            children=[
                html.Div(
                    className='sidebar div-for-slider five columns',
                    children=[ # SLIDERS AND DROPDOWNS
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[0]),
                                dcc.Slider(
                                    id='slider0',
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
                                    value=1
                                ),
                                html.Div(id='slider-output-container-0')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(bff15_labels[1]),
                                dcc.Slider(
                                    id='slider1',
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
                                    value=1
                                ),
                                html.Div(id='slider-output-container-1')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[2]),
                                dcc.Slider(
                                    id='slider2',
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
                                    value=1
                                ),
                                html.Div(id='slider-output-container-2')
                            ]
                        ),
                        html.Div(
                            children=[
                            html.H5(children=bff15_labels[3]),
                                dcc.Slider(
                                    id='slider3',
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
                                    value=1
                                ),
                                html.Div(id='slider-output-container-3')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[4]),
                                dcc.Slider(
                                    id='slider4',
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
                                    value=1
                                ),
                                html.Div(id='slider-output-container-4')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[5]),
                                dcc.Slider(
                                    id='slider5',
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
                                    value=1
                                ),
                                html.Div(id='slider-output-container-5')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[6]),
                                dcc.Slider(
                                    id='slider6',
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
                                    value=1
                                ),
                                # html.Div(id='slider-output-container-6')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[7]),
                                dcc.Slider(
                                    id='slider7',
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
                                    value=1
                                ),
                                # html.Div(id='slider-output-container-7')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[8]),
                                dcc.Slider(
                                    id='slider8',
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
                                    value=1
                                ),
                                # html.Div(id='slider-output-container-8')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[9]),
                                dcc.Slider(
                                    id='slider9',
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
                                    value=1
                                ),
                                # html.Div(id='slider-output-container-9')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[10]),
                                dcc.Slider(
                                    id='slider10',
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
                                    value=1
                                ),
                                # html.Div(id='slider-output-container-10')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[11]),
                                dcc.Slider(
                                    id='slider11',
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
                                    value=1
                                ),
                                # html.Div(id='slider-output-container-11')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[12]),
                                dcc.Slider(
                                    id='slider12',
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
                                    value=1
                                ),
                                # html.Div(id='slider-output-container-12')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[13]),
                                dcc.Slider(
                                    id='slider13',
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
                                    value=1
                                ),
                                # html.Div(id='slider-output-container-13')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5(children=bff15_labels[14]),
                                dcc.Slider(
                                    id='slider14',
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
                                    value=1
                                ),
                                # html.Div(id='slider-output-container-14')
                            ]
                        ),
                        
                        html.Div(
                            children=[
                                html.H5('Choose age:'),
                                dcc.Dropdown(
                                    id='Dem_age',
                                    options=[
                                        {'label': Dem_age, 'value': Dem_age}
                                        for Dem_age in range(18,110)
                                    ],
                                    clearable=False,
                                    value=40,
                                    style=dict(
                                        # paddingRight= 150,
                                        # width='75%',
                                        display='inline-block',
                                        verticalAlign="middle"
                                    )
                                )
                                # html.Div(id='slider-output-container-1')
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5("Pick a gender"),
                                dcc.Dropdown(
                                    id='Dem_gender',
                                    options=[
                                        {'label': Dem_gender, 'value': Dem_gender}
                                        for Dem_gender in np.sort(df.Dem_gender.unique())
                                    ],
                                    value='Other/would rather not say',
                                    clearable=False,
                                    style=dict(
                                        # paddingRight= 150,
                                        # width='75%',
                                        display='inline-block',
                                        verticalAlign="middle"
                                    )
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5("Pick your education"),
                                dcc.Dropdown(
                                    id='Dem_edu',
                                    options=[
                                        {'label': Dem_edu, 'value': Dem_edu}
                                        for Dem_edu in np.sort(df.Dem_edu.unique())
                                    ],
                                    value='None',
                                    clearable=False,
                                    style=dict(
                                        # paddingRight= 150,
                                        # width='75%',
                                        display='inline-block',
                                        verticalAlign="middle"
                                    )
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5("Pick your mother's education"),
                                dcc.Dropdown(
                                    id='Dem_edu_mom',
                                    options=[
                                        {'label': Dem_edu_mom, 'value': Dem_edu_mom}
                                        for Dem_edu_mom in np.sort(df.Dem_edu_mom.unique())
                                    ],
                                    value='None',
                                    clearable=False,
                                    style=dict(
                                        # paddingRight= 150,
                                        # width='75%',
                                        display='inline-block',
                                        verticalAlign="middle"
                                    )
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5("Pick your employment status"),
                                dcc.Dropdown(
                                    id='Dem_employment',
                                    options=[
                                        {'label': Dem_employment, 'value': Dem_employment}
                                        for Dem_employment in np.sort(df.Dem_employment.unique())
                                    ],
                                    value='Full time employed',
                                    clearable=False,
                                    style=dict(
                                        # paddingRight= 150,
                                        # width='75%',
                                        display='inline-block',
                                        verticalAlign="middle"
                                    )
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5("Are you living abroad?"),
                                dcc.Dropdown(
                                    id='Dem_Expat',
                                    options=[
                                        {'label': Dem_Expat, 'value': Dem_Expat}
                                        for Dem_Expat in np.sort(df.Dem_Expat.unique())
                                    ],
                                    value='no',
                                    clearable=False,
                                    style=dict(
                                        # paddingRight= 150,
                                        # width='75%',
                                        display='inline-block',
                                        verticalAlign="middle"
                                    )
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5("Choose your marital status"),
                                dcc.Dropdown(
                                    id='Dem_maritalstatus',
                                    options=[
                                        {'label': Dem_maritalstatus, 'value': Dem_maritalstatus}
                                        for Dem_maritalstatus in np.sort(df.Dem_maritalstatus.unique())
                                    ],
                                    value='Single',
                                    clearable=False,
                                    style=dict(
                                        # paddingRight= 150,
                                        # width='75%',
                                        display='inline-block',
                                        verticalAlign="middle"
                                    )
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5("Are you in a risk group?"),
                                dcc.Dropdown(
                                    id='Dem_riskgroup',
                                    options=[
                                        {'label': Dem_riskgroup, 'value': Dem_riskgroup}
                                        for Dem_riskgroup in np.sort(df.Dem_riskgroup.unique())
                                    ],
                                    value='No',
                                    clearable=False,
                                    style=dict(
                                        # paddingRight= 150,
                                        # width='75%',
                                        display='inline-block',
                                        verticalAlign="middle"
                                    )
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H5("Are you currently isolated?"),
                                dcc.Dropdown(
                                    id='Dem_isolation',
                                    options=[
                                        {'label': Dem_isolation, 'value': Dem_isolation}
                                        for Dem_isolation in np.sort(df.Dem_isolation.unique())
                                    ],
                                    value='1',
                                    clearable=False,
                                    style=dict(
                                        # paddingRight= 150,
                                        # width='75%',
                                        display='inline-block',
                                        verticalAlign="middle"
                                    )
                                ),
                            ],
                            style=dict(
                                paddingBottom='300px'
                            )
                        ),
                        
                    ]
                ),
#--------------------------------------------------------
# CHART SECTION
                html.Div(
                    className='chart-container five columns',
                    children=[ # CHART SECTION
                        html.Div(
                            className='row',
                            children=[
                                html.Div(
                                    className='six columns',
                                    children=[
                                        dcc.Graph( # PERSONALITY RADAR CHART
                                            id='personality-chart',
                                            config={"displayModeBar": False},
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className='three columns',
                                    children=[
                                        dash_table.DataTable( # TABLE PERSONALITY VALUES
                                            id='table',
                                            columns=[
                                                dict(id='Trait', name='Trait'),
                                                dict(
                                                    id='Score',
                                                    name='Score',
                                                    type='numeric',
                                                    format=Format(
                                                        precision=2,
                                                        scheme=Scheme.fixed
                                                        )
                                                    )
                                            ],
                                            style_as_list_view=True,
                                            style_cell={
                                                'padding': '5px',
                                                # 'fontSize': 18,
                                                },
                                            style_header={
                                                'backgroundColor': 'white',
                                                'fontWeight': 'bold'
                                            },
                                        ),
                                    ],
                                    style=dict(
                                        paddingTop=120
                                    )
                                )
                            ]
                        ),
                        html.Div(
                            className='row',
                            style=dict(
                                marginTop=-100
                            ),
                            children=[ 
                                html.Div(
                                    className='five columns',
                                    children=[
                                        dcc.Graph( # STRESS INDICATOR
                                            id='stress',
                                            config={"displayModeBar": False},
                                        )
                                    ]
                                ),
                                html.Div(
                                    className='five columns',
                                    children=[
                                        dcc.Graph( # LONELINESS INDICATOR
                                            id='loneliness',
                                            config={"displayModeBar": False},
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

@app.callback(
        
    [
        Output('personality-chart', 'figure'),
        Output('table', 'data')
    ],
    [
        Input('slider0', 'value'),
        Input('slider1', 'value'),
        Input('slider2', 'value'),
        Input('slider3', 'value'),
        Input('slider4', 'value'),
        Input('slider5', 'value'),
        Input('slider6', 'value'),
        Input('slider7', 'value'),
        Input('slider8', 'value'),
        Input('slider9', 'value'),
        Input('slider10', 'value'),
        Input('slider11', 'value'),
        Input('slider12', 'value'),
        Input('slider13', 'value'),
        Input('slider14', 'value'),
    
    ]
)


def update_chart(
    slider0, slider1, slider2, slider3, slider4, slider5,
    slider6, slider7, value8, slider9, slider10, slider11,
    slider12, slider13, slider14):
    
    df_predict = pd.DataFrame(
        columns=[
            'BFF_15_1','BFF_15_2', 'BFF_15_3', 'BFF_15_4', 'BFF_15_5', 'BFF_15_6',
            'BFF_15_7', 'BFF_15_8','BFF_15_9', 'BFF_15_10', 'BFF_15_11', 'BFF_15_12',
            'BFF_15_13', 'BFF_15_14', 'BFF_15_15'
        ],
        data=[[
            slider0, slider1, slider2, slider3, slider4, slider5,
            slider6, slider7, value8, slider9, slider10, slider11,
            slider12, slider13, slider14
        ]]
    )
    
    knn = load('models/knn.joblib')
    y_pred_log = knn.predict(
        df_predict
        # values.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
        )
    # y_pred = y_pred_log[0]
    prediction = pd.DataFrame(y_pred_log)
    prediction.columns = ['neu', 'ext', 'ope', 'agr', 'con']
    
    categories = ['NEU', 'OPE', 'EXT',
                'AGR', 'CONS','NEU']
    
    values = prediction.values.tolist()[0]
    values += values[:1]
    
    figure = go.Figure(
        data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself'
        )
    )
    figure.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[1, 6],
            ),
            angularaxis=dict(
                rotation=90,
                direction='counterclockwise'
            )
        ),
        showlegend=False,
        legend=dict(
            yanchor="top",
            y=1.4,
            xanchor="center",
            x=0.5,
            font=dict(
                size=18,
                # color="RebeccaPurple"
            )
        ),
        font=dict(
            # family="Gravitas One",
            # size=18,
            # color="RebeccaPurple"
        ),
        margin=dict(    
                l=70,
                r=80,
                b=20,
                t=20,
                pad=0
            ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'  
    )
    
    prediction_table = prediction.T.reset_index()
    prediction_table.columns=['Trait','Score']
    prediction_table.Trait = ['Neuroticism','Openness', 'Extraversion', 'Agreeableness', 'Conscientiousness']
    
    return figure, prediction_table.to_dict('records')

@app.callback(    
    [
        Output('stress', 'figure'),
        Output('loneliness', 'figure')
    ],
    [
        Input('slider0', 'value'),
        Input('slider1', 'value'),
        Input('slider2', 'value'),
        Input('slider3', 'value'),
        Input('slider4', 'value'),
        Input('slider5', 'value'),
        Input('slider6', 'value'),
        Input('slider7', 'value'),
        Input('slider8', 'value'),
        Input('slider9', 'value'),
        Input('slider10', 'value'),
        Input('slider11', 'value'),
        Input('slider12', 'value'),
        Input('slider13', 'value'),
        Input('slider14', 'value'),
        Input('Dem_age', 'value'),
        Input('Dem_gender', 'value'),
        Input('Dem_edu', 'value'),
        Input('Dem_edu_mom', 'value'),
        Input('Dem_employment', 'value'),
        Input('Dem_Expat', 'value'),
        Input('Dem_maritalstatus', 'value'),
        Input('Dem_riskgroup', 'value'),
        Input('Dem_isolation', 'value'),
    ]
)

def update_chart(
    slider0, slider1, slider2, slider3, slider4, slider5,
    slider6, slider7, value8, slider9, slider10, slider11,
    slider12, slider13, slider14, Dem_age, Dem_gender, Dem_edu, Dem_edu_mom,
    Dem_employment, Dem_Expat, Dem_maritalstatus, Dem_riskgroup, Dem_isolation
    ):
    
    df_predict = pd.DataFrame(
        columns=[
            'BFF_15_1', 'BFF_15_2', 'BFF_15_3', 'BFF_15_4', 'BFF_15_5', 'BFF_15_6',
            'BFF_15_7', 'BFF_15_8', 'BFF_15_9', 'BFF_15_10', 'BFF_15_11',
            'BFF_15_12', 'BFF_15_13', 'BFF_15_14', 'BFF_15_15',
            'Dem_age', 'Dem_gender', 'Dem_edu', 'Dem_edu_mom', 'Dem_employment',
            'Dem_Expat', 'Dem_maritalstatus', 'Dem_riskgroup', 'Dem_isolation'
        ],
        data=[
            [
            slider0, slider1, slider2, slider3, slider4, slider5,
            slider6, slider7, value8, slider9, slider10, slider11,
            slider12, slider13, slider14,
            Dem_age, Dem_gender, Dem_edu, Dem_edu_mom, Dem_employment, Dem_Expat,
            Dem_maritalstatus, Dem_riskgroup, Dem_isolation
            ]
        ]
    )
    
    model_stress = load('models/model_linear_stress.joblib')
    stress_y_pred_log = model_stress.predict(df_predict)
    stress_y_pred = stress_y_pred_log[0]
    
    fig_stress = go.Figure(go.Indicator(
        mode="gauge+number",
        value=stress_y_pred,
        title={'text': "Stress Level"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [None, 5]},
            'bar': {'color': "rgba(255, 56, 116, 1)"}}
    ))
    fig_stress.update_layout(
        margin=dict(
            l=40,
            r=40,
            b=0,
            t=0,
            pad=0
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)' 
    )
    
    model_loneliness = load('models/model_linear_loneliness.joblib')
    loneliness_y_pred_log = model_loneliness.predict(df_predict)
    loneliness_y_pred = loneliness_y_pred_log[0]
    
    fig_loneliness = go.Figure(go.Indicator(
        mode="gauge+number",
        value=loneliness_y_pred,
        title={'text': "Loneliness Level"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [None, 5]},
            'bar': {'color': "#97D9F3"}}
    ))
    fig_loneliness.update_layout(
        margin=dict(
            l=40,
            r=40,
            b=0,
            t=0,
            pad=0
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)' 
    )
    
    return fig_stress, fig_loneliness