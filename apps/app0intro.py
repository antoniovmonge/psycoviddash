import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

from app import app

# url='s3://psycovid/cleaned_data_040321.csv'
# df = pd.read_csv(url ,index_col=0)
df = pd.read_csv('raw_data/cleaned_data_040321.csv')

layout = html.Div([
    # html.H3('Intro', className='text-center'),
    html.H1('', className='text-padding'),
    dbc.Container([
    dbc.Row([
        dbc.Col(
            [
                html.H1('PSYCOVID - Data Science Project', className='text-center'), # bg-dark text-white
                dcc.Markdown(
                    '''
                    ##### Study based on on psychological impact and behavioural consequences of the COVID-19 outbreak
                    '''
                ),
                dcc.Markdown(
                    '''
                    ##### The Problem
                    
                    During the Covid-19 Outbreak, the world faced a new Stress and Loneliness levels. Those feelings affected the people in 
                    very different ways, depending on personality traces and demographic factors. Mental conditions such as depression, anxiety, paranoia became part
                    of the equation of the Outbreak.
                    '''
                ),
                dcc.Markdown(
                    '''
                    ##### How do we try to help with this problem?
                    
                    If we analyse the differnt personality tipes, the demographic factors and how those affect to the Stress and Perceived loneliness levels,
                    we could spot if a person is more able to suffer one or another mental condition and take action to prevent or reduce it thanks to recomendation systems, 
                    from what we learned through the collected data.
                    ''',
                    style=dict(marginTop=40)
                ),
                dcc.Markdown(
                    '''
                    ##### Tools
                    
                    DATA COLLECTION
                    The technolgy used for this Study is a SURVEY made between April and May 2021 that collected global data on the psychological and behavioural
                    impact of the COVID-19/coronavirus crisis.
                    '''
                )
            ],
            width=12
                )
    ]),
    dbc.Row(
        [
            dbc.Col(
                [
                    dcc.Markdown(
                        '''        
                        ##### Data Analysis
                                
                        Interactive Data Analysis of Personality and emotional repercusion 
                        of COVID-19 by countries. It allowus us to visualize and compare the
                        "mean personality", Stress and perceived Loneliness levels by countries.
                        
                        The Data Frame used in this project allows us the Analisys of demographic background variables,
                        perceived stress (PSS-10), availability of social provisions (SPS-10),
                        trust in various authorities, trust in governmental measures to contain the 
                        virus (OECD trust), personality traits (BFF-15), information behaviours, 
                        agreement with the level of government intervention, and compliance with 
                        preventive measures, along with a rich pool of exploratory variables and 
                        written experiences.
                        '''
                    ),
                    dcc.Markdown(
                        '''
                        ##### Predictions / Simulation
                        Interactive **Machine Learning** application that quantifies the personality based on the 
                        big 5 personality traits using the bff_personality test, and predict *stress* and 
                        *loneliness* levels based on personaliy and some demographical factors.
                        
                        It is possible to see how each imput affects to the "personality score" and Stress and Loneliness indicators.
                        
                        In order to cuantiffy the personality with the user input data, we used a [k-nearest neighbors regression algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm).
                        For the Stress and Loneliness levels the used algorithm is a [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression)
                        '''
                    ),
                ],
                style=dict(
                    paddingBottom= 200,
                    paddingRight= 70,
                )
        ),
        dbc.Col(
            [
                dcc.Markdown(
                    '''
                    ##### Data Source
                    
                    Data Collection Technology: **Survey** [COVIDiSTRESS Global Survey](https://osf.io/z39us/)
                    
                    Period of time Data Collection: between 30th March and 30th May 2020
                        
                    N = 173,426
                        
                    **Factor Types:**
                    - geographic location language 
                    - age of participant
                    - gouvernamental responses to the Coronavirus pandemic

                    **Measurements:** psychological measurement
                    - anxiety-related behavior trait
                    - Stress
                    - response to Isolation
                    - loneliness measurement
                    - Emotional Distress
                    '''
                )
            ],
            
        )
    ]),
]),
    
    ],)


@app.callback(
    Output('intro', 'children'),
    Input('app-intro-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)

