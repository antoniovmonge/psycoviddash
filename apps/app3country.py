import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import app

# url='s3://psycovid/cleaned_data_040321.csv'
# df = pd.read_csv(url ,index_col=0)
df = pd.read_csv('raw_data/cleaned_data_040321.csv',index_col=0)
# PREPARE DF
df_stress = df.groupby(['Country']).mean().reset_index()
df_stress_country = df_stress[['PSS10_avg', 'Country']].sort_values(
    by='PSS10_avg', ascending=True)

df_loneliness = df.groupby(['Country']).mean().reset_index()
df_loneliness_country = df_loneliness[['SLON3_avg', 'Country']].sort_values(
    by='SLON3_avg', ascending=True)
df_loneliness_country = df_loneliness_country.replace({'Country':'Bosnia and Herzegovina'},'B&H *')

# STRESS BAR CHART
stress_fig = px.bar(
    df_stress_country[-10:],
    y='Country',
    x='PSS10_avg',
    text='Country',
    height=400,
    title='STRESS levels by Country (Top 10)',
    labels={'PSS10_avg': 'Stress Level'},
    
)
stress_fig.update_traces(
    marker_color='rgb(158,202,225)',
    width=0.5,
    # marker_line_color='rgb(255, 0, 116)',
    # marker_line_width=1.5,
    # opacity=0.6,
    textposition='outside',
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    ),
)
stress_fig.update_layout(
    uniformtext_minsize=1,
    uniformtext_mode='hide',
    plot_bgcolor='rgb(244, 244, 244)',
    title={
        # "text": "Title Text",
        "x": 0.2,
        "xanchor": "left",
    }
    # paper_bgcolor='rgb(249, 246, 225)'
)        
stress_fig.update_xaxes(
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
    title='LONELINESS levels by Country (Top 10)',
    labels={'SLON3_avg': 'Loneliness Level'},
    
)
lonely_fig.update_traces(
    marker_color='rgb(158,202,225)',
    width=0.5,
    # marker_line_color='rgb(255, 0, 116)',
    # marker_line_width=1.5,
    # opacity=0.6,
    textposition='outside',
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    ),
)
lonely_fig.update_layout(
    uniformtext_minsize=1,
    uniformtext_mode='hide',
    plot_bgcolor='rgb(244, 244, 244)',
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
    children=[      
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='three columns div-user-controls', # Define the left element
                    children=[
                        html.H2('Analysis by Countries'),
                        html.P('''Visualising countries ranked '''),
                        html.P('''*B&H - Bosnia & Herzegovina''')
                    ],
                ),
                html.Div(
                    className='four columns', # Define the right element
                    children=[
                        dcc.Graph(
                            id='line-fig',
                            figure=stress_fig,
                            config={"displayModeBar": False},
                            className='card div-for-bar-charts'
                        ),
                        
                    ]
                ),
                html.Div(
                    className='four columns', # Define the right element
                    children=[
                        dcc.Graph(
                            id='line-fig',
                            figure=lonely_fig,
                            config={"displayModeBar": False},
                            className='card div-for-bar-charts'
                            ),   
                    ]
                )
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='three columns div-user-controls', # Define the left element
                    children=[
                        # html.H2('Analysis by Countries'),
                        # html.P('''Visualising countries ranked '''),
                        # html.P('''*B&H - Bosnia & Herzegovina''')
                    ],
                ),
                html.Div(
                    className='row',
                    children=[
                        html.Div(
                            className='eigth columns wrapper text-padding', # Define the left element
                            children=[
                                html.P(
                                    # className='menu',
                                    children='The Covid-19 pandemic sparked many changes...'
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
    Output('app-3-display-value', 'children'),
    Input('app-3-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)
