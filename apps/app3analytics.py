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

# url='s3://psycovid/cleaned_data_040321.csv'
# df = pd.read_csv(url ,index_col=0)
# df = pd.read_csv('raw_data/cleaned_data_040321.csv',index_col=0)
df = pd.read_csv('raw_data/cleaned_data_040321.csv',index_col=0)[['Country','PSS10_avg','SLON3_avg']]

# PREPARE DF
df_stress = df.groupby(['Country']).mean().reset_index()
df_stress_country = df_stress[['PSS10_avg', 'Country']].sort_values(
    by='PSS10_avg', ascending=True)

df_loneliness = df.groupby(['Country']).mean().reset_index()
df_loneliness_country = df_loneliness[['SLON3_avg', 'Country']].sort_values(
    by='SLON3_avg', ascending=True)
df_loneliness_country = df_loneliness_country.replace({'Country':'Bosnia and Herzegovina'},'B&H *')


# --------------------------------------------------
# STRESS BAR CHART
stress_fig = px.bar(
    df_stress_country[-10:],
    y='Country',
    x='PSS10_avg',
    text='Country',
    height=400,
    # title='STRESS levels (Top 10)',
    labels={'PSS10_avg': 'Stress Level'},
    
)
stress_fig.update_traces(
    # marker_color='rgb(158,202,225)',
    # marker_color=color_palette_list()[8],
    marker_color='#FF3874',
    width=0.4,
    # marker_line_color='rgb(255, 0, 116)',
    # marker_line_width=1.5,
    # opacity=0.6,
    textposition='outside',
    # hoverlabel=dict(
    #     bgcolor="white",
    #     font_size=16,
    #     font_family="Rockwell"
    # ),
)
stress_fig.update_layout(
    uniformtext_minsize=1,
    uniformtext_mode='hide',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0, 0, 0, 0.03)',
    # title={
    #     # "text": "Title Text",
    #     "x": 0.2,
    #     "xanchor": "left",
    # }
    # paper_bgcolor='rgb(249, 246, 225)'
)        
stress_fig.update_xaxes(
    range=[1, 5],
    showgrid=True,
    gridcolor='rgba(0, 0, 0, 0.1)',
    
    title_font_family='Helvetica',
    # linecolor= 'black',
    # linewidth= 0.5,
    # mirror=True,
    # ticks='outside',
)
# My personal trick to separate the y axis
stress_fig.update_yaxes(
    ticklabelposition='outside left',
    ticks="outside", tickwidth=2, tickcolor='white', ticklen=5,
    title_font_family='Helvetica',
    # linecolor= 'black',
    # linewidth= 0.5,
    # mirror=True,
)

# ---------------------------------------------------
# LONELINESS BAR CHART
lonely_fig = px.bar(
    df_loneliness_country[-10:],
    y='Country',
    x='SLON3_avg',
    text='Country',
    height=400,
    # title='LONELINESS levels (Top 10)',
    labels={'SLON3_avg': 'Loneliness Level'},
    
)
lonely_fig.update_traces(
    marker_color='#97D9F3',
    width=0.4,
    # marker_line_color='rgb(255, 0, 116)',
    # marker_line_width=1.5,
    # opacity=0.6,
    textposition='outside',
    # hoverlabel=dict(
    #     bgcolor="white",
    #     font_size=16,
    #     font_family="Rockwell"
    # ),
)
lonely_fig.update_layout(
    uniformtext_minsize=1,
    uniformtext_mode='hide',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0, 0, 0, 0.03)',
    # paper_bgcolor='rgb(249, 246, 225)',
    title={
        # "text": "Title Text",
        "x": 0.15,
        "xanchor": "left"
    }
)        
lonely_fig.update_xaxes(
    range=[1, 5],
    showgrid=True,
    gridcolor='rgb(224, 224, 224)',
    title_font_family='Helvetica',
    # linecolor= 'black',
    # linewidth= 0.5,
    # mirror=True,
    # ticks='outside',
)
# My personal trick to separate the y axis
lonely_fig.update_yaxes(
    ticklabelposition='outside left',
    ticks="outside", tickwidth=2, tickcolor='white', ticklen=5,
    title_font_family='Helvetica',
    # linecolor= 'black',
    # linewidth= 0.5,
    # mirror=True,
)

layout = html.Div(
    className='container',
    style=dict(
        paddingTop= 50,
        # paddingLeft= 100,
        # paddingRight= 100,
        # paddingBottom= 150,
    ),
    children=[      
        html.Div(
            className='row',
            children=[
                html.Div(
                    # className='div-user-controls', # Define the right element
                    children=[
                        dcc.Markdown('### Stress during the COVID-19 Pandemic by Countries'),
                        dcc.Markdown(
                            f'{paragraph1()}',
                        ),
                        
                    ]
                ),
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='six columns', # Define the left element
                    children=[
                        html.Div(
                            children=[
                                html.H6('STRESS levels (Top 10)'),
                            ],
                            style=dict(
                                textAlign='center'
                            )
                        ),
                        html.Div(
                            [
                                dcc.Graph(
                                    id='line-fig',
                                    figure=stress_fig,
                                    config={"displayModeBar": False},
                                    # style=dict(
                                    #     paddingLeft=120,
                                    #     paddingRight=120,
                                    # ),
                                ),
                            ],
                            style=dict(
                                marginTop=-60,
                            )
                        ),
                        
                    ],
                ),
                html.Div(
                    className='six columns', # Define the right element
                    children=[
                        dcc.Markdown('###### STRESS by Countries'),
                        dcc.Markdown('''Visualising countries ranked
                        with stress levels using the PSS-10 scale.
                        '''),
                        dcc.Markdown(
                            f'{paragraph2()}',
                        )      
                        # html.P('''* B&H - Bosnia & Herzegovina''')
                    ],
                    style=dict(
                        marginTop=30
                    )
                ),
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    children=[
                        dcc.Markdown('### Loneliness during the COVID-19 Pandemic by Countries'),
                        dcc.Markdown(
                            f'{paragraph3()}',
                        ) 
                    ],
                    style=dict(
                        paddingBottom=20,
                        paddingTop=20,
                    )
                ),
            ]
        ),
        # STAIC ANALYSIS LONELINESS
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='six columns',
                    children=[
                        html.Div(
                            children=[
                                html.H6('Percived LONELINESS levels (Top 10)'),
                            ],
                            style=dict(
                                textAlign='center'
                            ),
                        ),
                        html.Div(
                            children=[
                        
                                dcc.Graph(
                                    id='line-fig',
                                    figure=lonely_fig,
                                    config={"displayModeBar": False},
                                    # className='card div-for-bar-charts'
                                ),
                            ],
                            style=dict(
                                marginTop=-60,
                            )
                        ),
                    ]
                ),
                html.Div(
                    className='six columns', # Define the right element
                    children=[
                        dcc.Markdown('##### Analysis by Countries'),
                        html.P('''Visualising countries Loneliness ranked with the results of
                        UCLA short loneliness scale'''),
                        html.P('''*B&H - Bosnia & Herzegovina'''),
                        html.Div(
                            dcc.Markdown(
                                f'{paragraph4()}',
                            )       
                        )
                    ]    
                ),
            ]
        ),
    ],
)

