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
                # DROPDOWN COUNTRY 1
                html.Div(
                    className='three columns div-for-user-controls', # Define the left element
                    children=[
                        html.Div(
                            children='SELECT COUNTRY 1',
                            className='menu-title padding-top',
                            style={
                                # 'padding': '5px',
                                # 'fontSize': 18,
                                'textAlign': 'right'
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
                            className='text-padding-left',
                            style={
                                'paddingLeft': '50px',
                                # 'fontSize': 18,
                                'textAlign': 'right'
                            }
                        ),
                        # TABLE OF COUNTRY 1
                        html.Div(
                            className='text-padding-left',
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
                                    'fontSize': 18},
                                style_header={
                                    'backgroundColor': 'white',
                                    'fontWeight': 'bold'
                                },

                                )
                            ],
                            style={
                                'marginTop': 60,
                                # 'marginLeft': 60
                            }
                        ),
                    ]
                ),
                
                html.Div(
                    className='five columns',
                    children=[
                        dcc.Graph(
                            id='radar-chart',
                            config={"displayModeBar": False},
                            className='div-for-bar-charts',
                        )
                    ]
                ),
    # RADAR CHART --------------------------------
                html.Div(
                    className='three columns div-for-user-controls', # Define the left element
                    children=[
                        html.Div(
                            children='SELECT COUNTRY 2',
                            className='menu-title padding-top'
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
                            # className='text-padding-left',
                        ),
    # TABLE COUNTRY 2 ---------------------------
                        html.Div(
                            # className='text-padding-left',
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
                                    'fontSize': 18,
                                    'textAlign': 'left'
                                    },
                                style_header={
                                    'backgroundColor': 'white',
                                    'fontWeight': 'bold'
                                },

                                )
                            ],
                            style={
                                'marginTop': 60,
                                # 'marginLeft': 60
                            }
                        ),

                    ]
                ),
            ]
        ),
        
    ],
    style={
        'paddingLeft':20,
        'paddingRight':20
    }
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
    Output('table-2', 'data'),
    Input('country-filter-2', 'value')
)

def update_table(Country2):
    df_print = pd.DataFrame(df[df.Country == Country2][['neu','ope','ext','agr','con']].mean()).reset_index()
    df_print.columns = ['Trait', 'Score' ]
    df_print.Trait = ['Neuroticism','Openness', 'Extraversion', 'Agreeableness', 'Conscientiousness']
    return df_print.to_dict('records')
        