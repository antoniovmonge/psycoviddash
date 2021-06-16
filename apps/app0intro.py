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
        dbc.Col([html.H1('PSYCOVID - Data Science Project', className='text-center'), # bg-dark text-white
                dcc.Markdown(
                    '''
                    ##### Study based on on psychological impact and behavioural consequences of the COVID-19 outbreak
                    ''')],
                width=12
                )
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''        
                        #### Data Analysis
                        
                        Interactive Data Analysis of Personality and emotional repercusion 
                        of COVID-19 by countries
                        

                        Analisys of demographic background variables, perceived stress 
                        (PSS-10), availability of social provisions (SPS-10), trust in 
                        various authorities, trust in governmental measures to contain the 
                        virus (OECD trust), personality traits (BFF-15), information behaviours, 
                        agreement with the level of government intervention, and compliance with 
                        preventive measures, along with a rich pool of exploratory variables and 
                        written experiences.
                        '''
            ),
            dcc.Markdown(
                '''
                #### Predictions
                Interactive **Machine Learning** that quantifies you personality based on the 
                big 5 personality traits using the bff_personality test and predict *stress* and 
                *loneliness* levels based on your personaliy and some demographical factors.
                '''
            ),
        ]),
        dbc.Col([
            dcc.Markdown('''
                        ##### Data Source
                        
                        Data Collection Technology: **Survey** [COVIDiSTRESS Global Survey](https://osf.io/z39us/)
                            
                        > Period of time Data Collection: between 30th March and 30th May 2020
                            
                        > N = 173,426
                            
                        > Factor Types: 
                        - geographic location language 
                        - age of participant
                        - gouvernamental responses to the Coronavirus pandemic
                        
                        > Measurements: psychological measurement
                        - anxiety-related behavior trait
                        - Stress
                        - response to Isolation
                        - loneliness measurement
                        - Emotional Distress
                        ''')
        ])
    ]),
]),
    
    ],)


@app.callback(
    Output('intro', 'children'),
    Input('app-intro-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)

