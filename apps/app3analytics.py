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

# --------------------------------------------------
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
    # marker_color='rgb(158,202,225)',
    marker_color=color_palette_list()[8],
    width=0.5,
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
    plot_bgcolor='rgb(250, 250, 250)',
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
    # hoverlabel=dict(
    #     bgcolor="white",
    #     font_size=16,
    #     font_family="Rockwell"
    # ),
)
lonely_fig.update_layout(
    uniformtext_minsize=1,
    uniformtext_mode='hide',
    plot_bgcolor='rgb(250, 250, 250)',
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

# ------------------------------------
# LAYOUT
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
                    className='div-user-controls', # Define the right element
                    children=[
                        dcc.Markdown('### Stress during the COVID-19 Pandemic by Countries'),
                        dcc.Markdown(
                            f'{paragraph1()}',
                        ) 
                    ]
                ),
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='three columns div-user-controls', # Define the left element
                    children=[
                        dcc.Markdown('##### Analysis by Countries'),
                        dcc.Markdown('''Visualising countries ranked
                        with stress levels using the PSS-10 scale.
                        '''),
                        # html.P('''* B&H - Bosnia & Herzegovina''')
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
                    className='four columns text-padding-more',
                    children=[
                        html.Div(
                            # className='text-padding-more', # Define the left element
                                
                                dcc.Markdown(
                                    f'{paragraph2()}',
                                    className='text-padding-more',
                                )
                        
                                
                        )       
                    ]
                ),
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='div-user-controls', # Define the right element
                    children=[
                        dcc.Markdown('### Loneliness during the COVID-19 Pandemic by Countries'),
                        dcc.Markdown(
                            f'{paragraph3()}',
                        ) 
                    ]
                ),
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='three columns div-user-controls', # Define the left element
                    children=[
                        dcc.Markdown('##### Analysis by Countries'),
                        html.P('''Visualising countries Loneliness ranked with the results of
                        UCLA short loneliness scale'''),
                        html.P('''*B&H - Bosnia & Herzegovina''')
                    ],
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
                ),
                html.Div(
                    className='four columns text-padding-more',
                    children=[
                        html.Div(
                            dcc.Markdown(
                                f'{paragraph4()}',
                                className='text-padding-more',
                            )       
                        )   
                    ]
                ),
            ]
        ),
        # ---------------------------------------------------
        # TITLE NEW SECTION
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='div-user-controls',
                    children=[
                        dcc.Markdown('### Interactive analytics')
                    ]
                ),
            ]
        ),
        # COLUMNS WITH CONTENT
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='four columns div-for-user-controls', # Define the left element
                    children=[
                        html.Div(
                            children='SELECT COUNTRY',
                            className='menu-title text-padding-left padding-top'
                        ),
                        dcc.Dropdown(
                            id='country-filter',
                            options=[
                                {'label': Country, 'value': Country}
                                for Country in np.sort(df.Country.unique())
                            ],
                            value='Germany',
                            clearable=False,
                            className='text-padding-left',
                        ),
                    ]
                ),
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='five columns div-for-bar-charts',
                    children=[
                        dcc.Graph(
                            id='radar-chart',
                            config={"displayModeBar": False},
                            className='div-for-bar-charts',
                        )
                    ]
                ),
                html.Div(
                    className=''
                )
            ]
        ),      
    ]
)



@app.callback(
    Output('app-3-display-value', 'children'),
    Input('app-3-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('radar-chart', 'figure'),
    Input('country-filter', 'value')
)
def update_chart(Country):
    categories = ['Neuro', 'Open', 'Extro',
                'Agree', 'Cons', 'Neuro']

    radar_chart_figure = go.Figure()

    radar_chart_figure.add_trace(
        go.Scatterpolar(
            r=[
                df[df.Country == Country].groupby('Country')['neu'].mean()[0],
                df[df.Country == Country].groupby('Country')['ope'].mean()[0],
                df[df.Country == Country].groupby('Country')['ext'].mean()[0],
                df[df.Country == Country].groupby('Country')['agr'].mean()[0],
                df[df.Country == Country].groupby('Country')['con'].mean()[0],
                df[df.Country == Country].groupby('Country')['neu'].mean()[0],
            ],
            theta0=20,
            theta=categories,
            fill='toself',
            name=Country,
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
        showlegend=False,
        font=dict(
            # family="Courier New, monospace",
            # size=16,
            # color="RebeccaPurple"
        )
    )
    return radar_chart_figure