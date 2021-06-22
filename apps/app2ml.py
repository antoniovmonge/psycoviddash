import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_table
from dash_table.Format import Format, Scheme, Trim

import pickle
import numpy as np
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px

from app import app
from psycoviddash.functions import *

import __main__
# THIS THING MAKES THE JOBLIB WORK WITH FLASK APPS DEPLOYMENT
__main__.edu_func = edu_func
__main__.edu_mom_func = edu_mom_func
__main__.risk_group_func = risk_group_func
__main__.expat_func = expat_func

# url='s3://psycovid/cleaned_data_040321.csv'
# df = pd.read_csv(url ,index_col=0)

# df = pd.read_csv('raw_data/cleaned_data_040321.csv')
# df = df[df['Dem_isolation'] != '1']


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
        # paddingLeft=50,
        # paddingRight=100,
        width='90%',
    ),
    children=[
        html.Div(
            className='main-container',
            children=[
                html.Div(
                    className='sidebar card',
                    children=[
                        dcc.Markdown(
                            '''
                            #### Test for personality traits
                            1 = Strongly Disagree  
                            2 = Disagree  
                            3 = Slightly disagree  
                            4 = Slightly agree  
                            5 = Agree  
                            6 = Strongly Agree  
                            ''',
                            style=dict(
                                paddingBottom= 40,
                                textAlign= 'center',
                                ),
                        ),
                        dcc.Markdown(

                            '##### I see myself as a person who...',
                            style=dict(
                                paddingBottom= 20,
                                textAlign= 'center',
                                )
                        ),
                        html.Div(
                            className='div-for-slider',
                            children=[ # SLIDERS
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(bff15_labels[0]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(bff15_labels[1]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[2]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                    html.P(children=bff15_labels[3]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[4]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[5]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[6]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[7]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[8]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[9]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[10]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[11]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[12]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[13]),
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
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P(children=bff15_labels[14]),
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
                                    ]
                                ),
                        ]
                        ),
                        dcc.Markdown('#### Demographic Information'),
                        html.Div(
                            # className='div-for-dropdown',
                            children=[
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P('Choose age:'),
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
                                                # display='inline-block',
                                                # verticalAlign="middle"
                                            )
                                        )
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P("Pick a gender"),
                                        dcc.Dropdown(
                                            id='Dem_gender',
                                            options=[
                                                {'label': 'Female', 'value': 'Female'},
                                                {'label': 'Male', 'value': 'Male'},
                                                {'label': 'Other/would rather not say',
                                                'value': 'Other/would rather not say'}],
                                            # options=[
                                            #     {'label': Dem_gender, 'value': Dem_gender}
                                            #     for Dem_gender in np.sort(df.Dem_gender.unique())
                                            # ],
                                            value='Other/would rather not say',
                                            clearable=False,
                                            style=dict(
                                                # paddingRight= 150,
                                                # width='75%',
                                                # display='inline-block',
                                                # verticalAlign="middle"
                                            )
                                        ),
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P("Pick your education"),
                                        dcc.Dropdown(
                                            id='Dem_edu',
                                            options=[
                                                {'label': 'None', 'value': 'None'},
                                                {'label': 'Up to 6 years of school', 'value': 'Up to 6 years of school'},
                                                {'label': 'Up to 9 years of school', 'value': 'Up to 9 years of school'},
                                                {'label': 'Up to 12 years of school', 'value': 'Up to 12 years of school'},
                                                {'label': 'Some College, short continuing education or equivalent', 'value': 'Some College, short continuing education or equivalent'},
                                                {'label': 'College degree, bachelor, master',
                                                'value': 'College degree, bachelor, master'},
                                                {'label': 'PhD/Doctorate', 'value': 'PhD/Doctorate'},
                                                {'label': 'Uninformative response', 'value': 'Uninformative response'},
                                            ],
                                            # options=[
                                            #     {'label': Dem_edu, 'value': Dem_edu}
                                            #     for Dem_edu in np.sort(df.Dem_edu.unique())
                                            # ],
                                            value='None',
                                            clearable=False,
                                            style=dict(
                                                # paddingRight= 150,
                                                # width='75%',
                                                # display='inline-block',
                                                # verticalAlign="middle"
                                            )
                                        ),
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P("Pick your mother's education"),
                                        dcc.Dropdown(
                                            id='Dem_edu_mom',
                                            options=[
                                                {'label': 'None', 'value': 'None'},
                                                {'label': 'Up to 6 years of school', 'value': 'Up to 6 years of school'},
                                                {'label': 'Up to 9 years of school', 'value': 'Up to 9 years of school'},
                                                {'label': 'Up to 12 years of school', 'value': 'Up to 12 years of school'},
                                                {'label': 'Some College or equivalent', 'value': 'Some College or equivalent'},
                                                {'label': 'College degree', 'value': 'College degree'},
                                                {'label': 'PhD/Doctorate', 'value': 'PhD/Doctorate'},
                                                {'label': 'Uninformative response', 'value': 'Uninformative response'}
                                            ],
                                            # options=[
                                            #     {'label': Dem_edu_mom, 'value': Dem_edu_mom}
                                            #     for Dem_edu_mom in np.sort(df.Dem_edu_mom.unique())
                                            # ],
                                            value='None',
                                            clearable=False,
                                            style=dict(
                                                # paddingRight= 150,
                                                # width='75%',
                                                # display='inline-block',
                                                # verticalAlign="middle"
                                            )
                                        ),
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P("Pick your employment status"),
                                        dcc.Dropdown(
                                            id='Dem_employment',
                                            options=[
                                                {'label': 'Student', 'value': 'Student'},
                                                {'label': 'Retired', 'value': 'Retired'},
                                                {'label': 'Part time employed', 'value': 'Part time employed'},
                                                {'label': 'Not employed', 'value': 'Not employed'},
                                                {'label': 'Full time employed', 'value': 'Full time employed'},
                                                {'label': 'Self-employed', 'value': 'Self-employed'}
                                            ],
                                            # options=[
                                            #     {'label': Dem_employment, 'value': Dem_employment}
                                            #     for Dem_employment in np.sort(df.Dem_employment.unique())
                                            # ],
                                            value='Full time employed',
                                            clearable=False,
                                            style=dict(
                                                # paddingRight= 150,
                                                # width='75%',
                                                # display='inline-block',
                                                # verticalAlign="middle"
                                            )
                                        ),
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P("Are you living abroad?"),
                                        dcc.Dropdown(
                                            id='Dem_Expat',
                                            options=[
                                                {'label': 'Yes', 'value': 'yes'},
                                                {'label': 'No', 'value': 'no'}
                                            ],
                                            # options=[
                                            #     {'label': Dem_Expat, 'value': Dem_Expat}
                                            #     for Dem_Expat in np.sort(df.Dem_Expat.unique())
                                            # ],
                                            value='no',
                                            clearable=False,
                                            style=dict(
                                                # paddingRight= 150,
                                                # width='75%',
                                                # display='inline-block',
                                                # verticalAlign="middle"
                                            )
                                        ),
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P("Choose your marital status"),
                                        dcc.Dropdown(
                                            id='Dem_maritalstatus',
                                            options=[
                                                {'label': 'Single', 'value': 'Single'},
                                                {'label': 'Married/cohabiting', 'value': 'Married/cohabiting'},
                                                {'label': 'Other or would rather not say', 'value': 'Other or would rather not say'},
                                                {'label': 'Divorced/widowed', 'value': 'Divorced/widowed'},
                                                {'label': 'Uninformative response', 'value': 'Uninformative response'}
                                            ],
                                            # options=[
                                            #     {'label': Dem_maritalstatus, 'value': Dem_maritalstatus}
                                            #     for Dem_maritalstatus in np.sort(df.Dem_maritalstatus.unique())
                                            # ],
                                            value='Single',
                                            clearable=False,
                                            style=dict(
                                                # paddingRight= 150,
                                                # width='75%',
                                                # display='inline-block',
                                                # verticalAlign="middle"
                                            )
                                        ),
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=20
                                    ),
                                    children=[
                                        html.P("Are you in a risk group?"),
                                        dcc.Dropdown(
                                            id='Dem_riskgroup',
                                            options=[
                                                {'label': 'Yes','value': 'Yes'},
                                                {'label': 'No','value': 'No'},
                                                {'label': 'Not sure','value': 'Not sure'}
                                            ],
                                            # options=[
                                            #     {'label': Dem_riskgroup, 'value': Dem_riskgroup}
                                            #     for Dem_riskgroup in np.sort(df.Dem_riskgroup.unique())
                                            # ],
                                            value='No',
                                            clearable=False,
                                            style=dict(
                                                # paddingRight= 150,
                                                # width='75%',
                                                # display='inline-block',
                                                # verticalAlign="middle",
                                                # fontSize=12,
                                                # # marginLeft= '5px',
                                                # # paddingLeft= '100px',
                                                # textAlign= 'center',
                                                # width='90%',
                                                # heigh=10,
                                                # display='right',
                                                # # verticalAlign="right",
                                            )
                                        ),
                                    ]
                                ),
                                html.Div(
                                    style=dict(
                                        paddingBottom=800,
                                    ),
                                    children=[
                                        html.P("Are you currently isolated?"),
                                        dcc.Dropdown(
                                            id='Dem_isolation',
                                            options=[
                                                {'label': 'Isolated', 'value': 'Isolated'},
                                                {'label': 'Life carries on with minor changes', 'value': 'Life carries on with minor changes'},
                                                {'label': 'Life carries on as usual', 'value': 'Life carries on as usual'},
                                                {'label': 'Isolated in medical facility of similar location', 'value':'Isolated in medical facility of similar location'}
                                            ],
                                            # options=[
                                            #     {'label': Dem_isolation, 'value': Dem_isolation}
                                            #     for Dem_isolation in np.sort(df.Dem_isolation.unique())
                                            # ],
                                            value='Isolated',
                                            clearable=False,
                                        ),
                                    ],

                                ),
                    ]

                ),


                    ]
                ),
                #--------------------------------------------------------
                # CHART SECTION
                html.Div(
                    className='chart-container',
                    children=[ # CHART SECTION
                        html.Div(
                            # className='container',
                            children=[
                                html.Div(
                                    className='row',
                                    children=[
                                        html.Div(
                                            className='ten columns offset-by-two columns',
                                            style=dict(
                                                marginTop=20,
                                                marginBottom=-20,
                                            ),
                                            children=[
                                                html.P(
                                                    'BIG 5 PERSONALITY SCORES',
                                                    style=dict(textAlign='center')
                                                ),
                                            ]
                                        ),
                                        html.Div( # RADAR CHART
                                            className='six columns offset-by-two columns',
                                            style=dict(
                                                marginTop=-60,
                                                marginBottom=-60,
                                            ),
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
                                                paddingTop=60
                                            )
                                        )
                                    ],
                                ),
                                # html.Div( # TITLE STRESS AND LONELINESS INDICATORS
                                #     className = 'ten columns offset-by-two columns',
                                #     style=dict(
                                #         textAlign='center',
                                #         marginBottom=-80,
                                #     ),
                                #     children=[
                                #         html.H6('IN A PANDEMIC OUTBREAK,'),
                                #         html.P('the prediction about your Stress and Loneliness levels is:')
                                #     ]
                                # ),
                                html.Div(
                                    className='row',
                                    style=dict(
                                        marginTop=-100
                                    ),
                                    children=[
                                        html.Div(
                                            className='five columns offset-by-two columns',
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
                        ),

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


def update_chart_1(
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

    knn = joblib.load('models/knn.joblib')
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
                l=100,
                r=100,
                b=0,
                t=0,
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

def update_chart_2(
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

    model_stress = joblib.load('models/model_linear_stress_3.joblib')
    # model_stress = pickle.load(open('models/stress_pipeline.pkl','rb'))
    stress_y_pred_log = model_stress.predict(df_predict)
    stress_y_pred = stress_y_pred_log[0]

    fig_stress = go.Figure(go.Indicator(
        mode="gauge+number",
        value=stress_y_pred,
        title={'text': "Stress Level"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 5]},
            'bar': {'color': "rgba(255, 56, 116, 1)"},
            'steps': [
                {'range': [0,2.4], 'color': 'rgba(142, 219, 157, 0.1)'},
                {'range': [2.4,3.7], 'color': 'rgba(255, 167, 5, 0.1)'},
                {'range': [3.7,5], 'color': 'rgba(255, 5, 5, 0.1)'},
            ]
            }
    ))
    fig_stress.update_layout(
        margin=dict(
            l=70,
            r=70,
            b=40,
            t=0,
            pad=0
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    model_loneliness = joblib.load('models/model_linear_loneliness_3.joblib')
    # model_loneliness = pickle.load(open('models/loneliness_pipeline.pkl', 'rb'))
    loneliness_y_pred_log = model_loneliness.predict(df_predict)
    loneliness_y_pred = loneliness_y_pred_log[0]

    fig_loneliness = go.Figure(go.Indicator(
        mode="gauge+number",
        value=loneliness_y_pred,
        title={'text': "Loneliness Level"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 5]},
            'bar': {'color': "#97D9F3"},
            'steps': [
                {'range': [0,2.4], 'color': 'rgba(142, 219, 157, 0.1)'},
                {'range': [2.4,3.7], 'color': 'rgba(255, 167, 5, 0.1)'},
                {'range': [3.7,5], 'color': 'rgba(255, 5, 5, 0.1)'},
            ]
        }
    ))
    fig_loneliness.update_layout(
        margin=dict(
            l=70,
            r=70,
            b=40,
            t=0,
            pad=0
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    return fig_stress, fig_loneliness