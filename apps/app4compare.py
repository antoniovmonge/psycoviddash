import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from psycoviddash.textapp import *
from psycoviddash.colors import color_palette_list
import numpy as np
import plotly.graph_objects as go
import dash_table
from dash_table.Format import Format, Scheme, Trim

from app import app
# from functions import *

df = pd.read_csv('raw_data/cleaned_data_040321.csv',index_col=0)[['Country','PSS10_avg','SLON3_avg','neu','ext','ope','agr','con']]

layout = html.Div(
    # className='Container',
    style=dict(
        paddingLeft= 100,
        paddingRight= 100,
        marginBottom= 150,
    ),
    children=[
        html.Div(
            className='row',
            style=dict(
                marginTop=30
            ),
            children=[
                html.Div(
                    className='col',
                    children=[
                        html.H3(
                            'Country Mean Personality Traits', className='text-center'),
                    ]
                )
            ]
        ),
        # COLUMNS WITH CONTENT
        html.Div(
            className='row',
            children=[
                # DROPDOWN COUNTRY 1
                html.Div(
                    className='four columns',
                    style=dict(
                        textAlign='right',
                        # paddingTop='50px',
                        paddingLeft='200px',
                    ),
                    children=[
                        html.Div(
                            children='SELECT COUNTRY 1',
                            className='menu-title padding-top',
                            style={
                                # 'paddingLeft': '5px',
                                # 'fontSize': 18,
                                'textAlign': 'center',
                                'paddingBottom': '10px'
                            }
                        ),
                        dcc.Dropdown(
                            id='country-filter-1',
                            options=[
                                {'label': Country, 'value': Country}
                                for Country in np.sort(df.Country.unique())
                            ],
                            value='Germany',
                            clearable=False,
                            # className='text-padding-left',
                            # style={
                            #     'paddingLeft': '150px',
                            #     # 'fontSize': 18,
                            #     'textAlign': 'right'
                            # },
                            style=dict(
                                # marginLeft= '5px',
                                # paddingLeft= '100px',
                                textAlign= 'center',
                                # width='90%',
                                # display='right',
                                # verticalAlign="right",
                                # display='inline-block',
                                verticalAlign="middle"
                            )
                        ),
                        html.Div(
                            className='div-for-table',
                            children=[
                                dash_table.DataTable(
                                    id='table-1',
                                    columns=[
                                        dict(id='Trait', name='Trait'),
                                        dict(id='Score', name='Score', type='numeric', format=Format(precision=2, scheme=Scheme.fixed))
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
                                paddingTop='50px'
                            )
                        )
                        
                    ],
                ),
                # RADAR CHART --------------------------------
                html.Div(
                    className='four columns',
                    style=dict(
                        marginTop=0
                    ),
                    children=[
                        dcc.Graph(
                            id='radar-chart',
                            config={"displayModeBar": False},
                            className='div-for-bar-charts',
                        )
                    ]
                ),
                
                html.Div(
                    className='four columns div-for-user-controls', # Define the left element
                    style=dict(
                        textAlign='left',
                        paddingRight='200px',
                        # paddingTop='50px'
                    ),
                    children=[
                        html.Div(
                            children='SELECT COUNTRY 2',
                            className='menu-title padding-top',
                            style={
                                # 'paddingLeft': '5px',
                                # 'fontSize': 18,
                                'textAlign': 'center',
                                'paddingBottom': '10px'
                            }
                        ),
                        # DROPDOWN COUNTRY 2 -------------------------
                        dcc.Dropdown(
                            id='country-filter-2',
                            options=[
                                {'label': Country, 'value': Country}
                                for Country in np.sort(df.Country.unique())
                            ],
                            value='Taiwan',
                            clearable=False,
                            style=dict(
                                # paddingRight= 150,
                                textAlign= 'center',
                                # width='75%',
                                # display='inline-block',
                                verticalAlign="middle",
                            )
                            # className='text-padding-left',
                        ),
                        html.Div(
                            className='div-for-table',
                            children=[
                                dash_table.DataTable(
                                    id='table-2',
                                    columns=[
                                    
                                        dict(id='Score', name='Score', type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
                                        dict(id='Trait', name='Trait')
                                    ],
                                    style_as_list_view=True,
                                    style_cell={
                                        'padding': '5px',
                                        # 'fontSize': 18,
                                        'textAlign': 'left'
                                        },
                                    style_header={
                                        'backgroundColor': 'white',
                                        'fontWeight': 'bold'
                                    },
                                ),
                            ],
                            style=dict(
                                paddingTop='50px'
                            )
                        )
                        
                    ]
                ),  
            ]
        ),
        # INDICATORS
        html.Div(
            className='row',
            children=[
                # COLUMN 1
                html.Div(
                    className='two columns offset-by-one column',
                    children=[
                        html.Div(
                            className='column',
                            children=[
                                
                                dcc.Graph(
                                    id='stress-1',
                                    config={"displayModeBar": False},
                                )
                            ],
                            style=dict(
                                marginTop= 10,
                                # marginLeft= 200,
                            ),
                        ),
                    ],
                ),
                html.Div(
                    className='two columns',
                    children=[
                        html.Div(
                            className='column',
                            children=[
                                
                                dcc.Graph(
                                    id='loneliness-1',
                                    config={"displayModeBar": False},
                                )
                            ],
                            style=dict(
                                marginTop= 10,
                                # marginLeft= 200,
                            ),
                        ),
                    ],
                ),
                # SEPARATOR
                html.Div(
                    className='two columns',
                    children=[
                        html.Div(' ')
                    ]
            
                ),
                # COLUMN 2
                html.Div(
                    className='two columns',
                    children=[
                        html.Div(
                            className='column',
                            children=[
                                
                                dcc.Graph(
                                    id='stress-2',
                                    config={"displayModeBar": False},
                                )
                            ],
                            style=dict(
                                marginTop= 10,
                                # marginLeft= 120,
                            ),     
                        ),
                    ]
                ),
                html.Div(
                    className='two columns',
                    children=[
                        html.Div(
                            className='column',
                            children=[           
                                dcc.Graph(
                                    id='loneliness-2',
                                    config={"displayModeBar": False},
                                )
                            ],
                            style=dict(
                                marginTop= 10,
                                # marginLeft= 120,
                            ),     
                        ),
                    ]
                ),
            ],
            style=dict(
                marginTop='-150px',
                paddingLeft='100px',
                paddingRight='100px',
            )
        ),
        
        
    ],
)

@app.callback(
    
        Output('radar-chart', 'figure'),
    [
        Input('country-filter-1', 'value'),
        Input('country-filter-2', 'value'),
    ]
)
def update_chart(Country1, Country2):
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

    radar_chart_figure.add_trace(
        go.Scatterpolar(
            r=[
                df[df.Country == Country2].groupby('Country')['neu'].mean()[0],
                df[df.Country == Country2].groupby('Country')['ope'].mean()[0],
                df[df.Country == Country2].groupby('Country')['ext'].mean()[0],
                df[df.Country == Country2].groupby('Country')['agr'].mean()[0],
                df[df.Country == Country2].groupby('Country')['con'].mean()[0],
                df[df.Country == Country2].groupby('Country')['neu'].mean()[0],
            ],
            theta=categories,
            fill='toself',
            name=Country2,
            # line_color='rgba(148, 224, 243, 0.56)'
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
            y=1.3,
            xanchor="center",
            x=0.5,
            font=dict(
                # family="Gravitas One",
                size=12,
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

@app.callback(
    Output('table-1', 'data'),
    Input('country-filter-1', 'value')
)

def update_table(Country1):
    df_print = pd.DataFrame(df[df.Country == Country1][['neu','ope','ext','agr','con']].mean()).reset_index()
    df_print.columns = ['Trait', 'Score' ]
    df_print.Trait = ['Neuroticism','Openness', 'Extraversion', 'Agreeableness', 'Conscientiousness']
    return df_print.to_dict('records')

@app.callback(
    Output('stress-1', 'figure'),
    Input('country-filter-1', 'value')
    )

def update_chart(Country1):
    figure_stress_1 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = df[df.Country == Country1]['PSS10_avg'].mean(),
        title = {'text': "Stress"},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge=dict(
            axis= {'range': [None, 5]},
            bar= {'color': "rgb(255, 56, 116)"},
            steps= [
                # {'range': [0, 2.4], 'color': '#DFC4AA'},
                # {'range': [2.4, 3.7], 'color': '#F38C71'},
                # {'range': [3.7, 5], 'color': '#EE5344'}
                ],
        )
    ))
    figure_stress_1.update_layout(
        margin=dict(    
            l=20,
            r=20,
            b=0,
            t=0,
            pad=0
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'  
    )
    return figure_stress_1

@app.callback(
    Output('loneliness-1', 'figure'),
    Input('country-filter-1', 'value')
    )

def update_chart(Country1):
    figure_loneliness_1 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = df[df.Country == Country1]['SLON3_avg'].mean(),
        title = {'text': "Loneliness"},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge=dict(
            axis= {'range': [None, 5]},
            bar= {'color': "#add8e6"},
            steps= [
                # {'range': [0, 2.4], 'color': '#DFC4AA'},
                # {'range': [2.4, 3.7], 'color': '#F38C71'},
                # {'range': [3.7, 5], 'color': '#EE5344'}
                ],
        )
    ))
    figure_loneliness_1.update_layout(
        margin=dict(    
            l=20,
            r=20,
            b=0,
            t=0,
            pad=0
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return figure_loneliness_1

@app.callback(
    Output('table-2', 'data'),
    Input('country-filter-2', 'value')
)

def update_table(Country2):
    df_print = pd.DataFrame(df[df.Country == Country2][['neu','ope','ext','agr','con']].mean()).reset_index()
    df_print.columns = ['Trait', 'Score' ]
    df_print.Trait = ['Neuroticism','Openness', 'Extraversion', 'Agreeableness', 'Conscientiousness']
    return df_print.to_dict('records')

@app.callback(
    Output('stress-2', 'figure'),
    Input('country-filter-2', 'value')
)
def update_chart(Country2):
    figure_stress_2 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = df[df.Country == Country2]['PSS10_avg'].mean(),
        title = {'text': "Stress"},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge=dict(
            axis= {'range': [None, 5]},
            bar= {'color': "rgb(255, 56, 116)"}
        )
    ))
    figure_stress_2.update_layout(
        margin=dict(    
            l=20,
            r=20,
            b=0,
            t=0,
            pad=0
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return figure_stress_2

@app.callback(
    Output('loneliness-2', 'figure'),
    Input('country-filter-2', 'value')
    )

def update_chart(Country2):
    figure_loneliness_2 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = df[df.Country == Country2]['SLON3_avg'].mean(),
        title = {'text': "Loneliness"},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge=dict(
            axis= {'range': [None, 5]},
            bar= {'color': "#add8e6"},
            steps= [
                # {'range': [0, 2.4], 'color': '#DFC4AA'},
                # {'range': [2.4, 3.7], 'color': '#F38C71'},
                # {'range': [3.7, 5], 'color': '#EE5344'}
                ],
        )
    ))
    figure_loneliness_2.update_layout(
        margin=dict(    
            l=20,
            r=20,
            b=0,
            t=0,
            pad=0
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
        )
    return figure_loneliness_2