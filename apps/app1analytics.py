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
from psycoviddash.functions import *

# LOAD DATA FRAME FROM AWS S3
url='s3://psycovid/cleaned_data_040321.csv'
df = pd.read_csv(url, index_col=0)[[
    'Country', 'PSS10_avg', 'SLON3_avg', 'Dem_age', 'Dem_gender',
    'Dem_employment'
]].replace({'Dem_gender': 'Other/would rather not say'}, 'Other')
# df = pd.read_csv('raw_data/cleaned_data_040321.csv',index_col=0)

# df = pd.read_csv('raw_data/cleaned_data_040321.csv', index_col=0)[[
#     'Country', 'PSS10_avg', 'SLON3_avg', 'Dem_age', 'Dem_gender',
#     'Dem_employment'
# ]].replace({'Dem_gender': 'Other/would rather not say'}, 'Other')

# SURVEY PART #######################################################
# GENDER PIE CHART FIG 1
color_palette_list = [
    '#CDF1AE', '#90DACC', '#F7E9D1', '#F4D2B5', '#EAB7B7', '#B89ACF'
]
# values = list(df['Dem_gender'].value_counts(normalize=True))
# names = list(df['Dem_gender'].value_counts().index)
fig1 = px.pie(
    df,
    values=list(df['Dem_gender'].value_counts(normalize=True)),
    names=list(df['Dem_gender'].value_counts().index))
fig1.update_traces(
    textposition='outside',
    textinfo='percent+label',
    marker=dict(colors=color_palette_list))
fig1.update_layout(
    # autosize=False,
    # width=300,
    # height=200,
    showlegend=False,
    margin=dict(l=0, r=0, b=0, t=0, pad=0),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')

# EMPLOYMENT PIE CHART
fig2 = px.pie(
    df,
    values=list(df['Dem_employment'].value_counts(normalize=True)),
    names=list(df['Dem_employment'].value_counts().index)
    )
fig2.update_traces(
    textposition='inside',
    textinfo='percent+label',
    marker=dict(colors=color_palette_list)
    )
fig2.update_layout(
    showlegend=False,
    margin=dict(l=30, r=30, b=0, t=0, pad=4),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
    )

# TABLE GENDER
# df_gender = pd.DataFrame(
#     (df['Dem_gender'].value_counts(normalize=True)))
# df_gender.columns = ['%']

# GENDER TABLE
df_gender = df[['Dem_gender']].copy()
df_gender = pd.DataFrame(
    (df['Dem_gender'].value_counts(normalize=True).round(3) * 100)).reset_index()
df_gender.columns = ['Gender', '%']
df_gender = df_gender.replace({'Gender': 'Other/would rather not say'}, 'Other')
# df_gender['%']=pd.Series(["{0:.2f}".format(val * 100) for val in df_gender['%']], index = df_gender.index)

# EMPLOYMENT TABLE
df_employment = df[['Dem_employment']].copy()
df_employment = pd.DataFrame(
    (df['Dem_employment'].value_counts(normalize=True).round(3) * 100)).reset_index()
df_employment.columns = ['Empl. Status', '%']
# df_employment['%'] = (df_employment['%'] / df_employment['%'].sum() * 100)

# AGE CHART
data_age = df.Dem_age.value_counts()
fig3 = px.bar(
    data_age,
    labels={
        'index': 'Age',
        'value': 'Count'
    },
    template="simple_white")
fig3.update_traces(marker=dict(color=color_palette_list[1]))
fig3.update_layout(
    # autosize=False,
    # width=600,
    height=250,
    showlegend=False,
    margin=dict(l=40, r=40, b=0, t=0, pad=0),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
fig3.update_yaxes(showgrid=True)

# AGE TABLE
d = {
    'Summary': ['Mean', 'Median', 'Mode', 'Min', 'Max'],
    'Value': [
        df[['Dem_age']].mean()[0].round(2), df[['Dem_age']].median()[0],
        df['Dem_age'].mode()[0], df[['Dem_age']].min()[0],
        df[['Dem_age']].max()[0]
    ]
}
df_age_summary = pd.DataFrame(data=d)

#####################################################################

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
        # paddingTop= 50,
        # paddingLeft= 100,
        # paddingRight= 100,
        paddingBottom=200, ),
    children=[
        html.Div(  # SURVEY ANALYSIS
            children=[
                html.Div(  # TITLE TAB
                    className='twelve columns',
                    children=[
                        dcc.Markdown('''
                        ## SURVEY ANALYSIS  
                        #### Characteristics of the respondants
                        ''',
                                     className='text-center')
                    ],
                    style=dict(
                        # textAlign='center',
                        marginTop=35,
                        marginBottom=35)),
                html.Div(  # 1ST ROW
                    className='row',
                    children=[
                        html.Div(  # LEFT COLUMN
                            className='six columns',
                            style=dict(paddingRight=100),
                            children=[
                                html.Div(
                                    [
                                        dcc.Markdown('''
                                        ###### Gender of respondents percentage distribution
                                        ''',
                                                     # className='text-center'
                                                     ),
                                        dcc.Markdown(f'''
                                        Respondents were {72.08} % female, 26.89 % Male. The remaining respondents answered 'other' or did not provide an answer.
                                        ''',
                                                     # style={'marginTop': 75}
                                                     )
                                    ],
                                    # style={'marginTop': 30}
                                ),
                                html.Div([
                                    # SECTION 1 CHART
                                    html.Div(
                                        className='six columns',
                                        children=[
                                            html.Div(
                                                style=dict(
                                                    marginTop=-100,
                                                    marginBottom=-75,
                                                    marginLeft=20,
                                                ),
                                                children=[
                                                    dcc.Graph(
                                                        id='pie-chart',
                                                        figure=fig1,
                                                        config={
                                                            "displayModeBar":
                                                            False
                                                        },
                                                    )
                                                ]),
                                        ],
                                    ),
                                    # TABLE (LEFT COLUMN)
                                    html.Div(
                                        className=
                                        'four columns offset-by-one column',
                                        children=[
                                            html.Div(children=[
                                                dash_table.DataTable(
                                                    id='table',
                                                    columns=[
                                                        dict(id='Gender',
                                                             name='Gender'),
                                                        dict(id='%',
                                                             name='%',
                                                             type='numeric',
                                                             format=Format(
                                                                 precision=2,
                                                                 scheme=Scheme.
                                                                 fixed))
                                                    ],
                                                    data=df_gender.to_dict(
                                                        'records'),
                                                    style_as_list_view=True,
                                                    style_cell={
                                                        'padding': '5px'
                                                    },
                                                    style_header={
                                                        'backgroundColor':
                                                        'white',
                                                        'fontWeight': 'bold'
                                                    },
                                                ),
                                            ],
                                                     style={'marginTop': 50}),
                                        ],
                                    ),
                                ]),
                            ]),
                        html.Div(  # RIGHT COLUMN
                            className='six columns',
                            children=[
                                html.Div(  # Section Title
                                    [
                                        dcc.Markdown('''
                                        ###### Employment Status of respondents percentage distribution
                                        ''',
                                                     # className='text-center'
                                                     ),
                                        dcc.Markdown(
                                            f'''
                                        The majority of the respondents ({(float(df_employment.iloc[0]['%']) + float(df_employment.iloc[2]['%']) + 
                                        float(df_employment.iloc[3]['%'])) }%) 
                                        were in full-time, part-time or self-employed, ({(float(df_employment.iloc[4]['%']) + float(df_employment.iloc[5]['%']))}%) 
                                        were either unemployed or retired, {float(df_employment.iloc[1]['%'])}% were students.
                                        ''',  # style={'marginTop': 125}
                                        )
                                    ],
                                    style={
                                        # 'marginTop': 50,
                                        'marginBottom': 50
                                    }),
                                html.Div(
                                    className='row',
                                    children=[
                                        html.Div(
                                            className='five columns',
                                            style=dict(marginTop=-125,
                                                       marginBottom=-75),
                                            children=[
                                                html.Div(
                                                    dcc.Graph(
                                                        id='pie-chart-2',
                                                        figure=fig2,
                                                        config={
                                                            "displayModeBar":
                                                            False
                                                        },
                                                    )),
                                            ]),
                                        html.Div(
                                            className=
                                            'four columns offset-by-two columns',
                                            children=[
                                                dash_table.DataTable(
                                                    id='table-2',
                                                    columns=[
                                                        dict(
                                                            id='Empl. Status',
                                                            name=
                                                            'Employment Status'
                                                        ),
                                                        dict(id='%',
                                                             name='%',
                                                             type='numeric',
                                                             format=Format(
                                                                 precision=2,
                                                                 scheme=Scheme.
                                                                 fixed))
                                                    ],
                                                    data=df_employment.to_dict(
                                                        'records'),
                                                    style_as_list_view=True,
                                                    style_cell={
                                                        'padding': '5px'
                                                    },
                                                    style_header={
                                                        'backgroundColor':
                                                        'white',
                                                        'fontWeight': 'bold'
                                                    },
                                                ),
                                            ]),
                                    ]),
                                html.Div()
                            ]),
                    ]),
                html.Div(
                    className='row',
                    children=[
                        html.Div(
                            className='twelve columns',
                            children=[
                                dcc.Markdown(
                                    '''
                                        ###### Age of respondents 
                                        ''',
                                    # className='text-center',
                                    style=dict(marginTop=40)),
                                dcc.Markdown(f'''
                                The age of the respondents ranged from {df[['Dem_age']].min()[0]} to {df[['Dem_age']].max()[0]}, with a median age of {int(df[['Dem_age']].median()[0])}.
                                The age that appears more offen is {df['Dem_age'].mode()[0]}.
                                ''',
                                             style={
                                                 'marginTop': 0,
                                                 'marginBottom': 30
                                             }),
                                html.Div(
                                    className='row',
                                    children=[
                                        html.Div(
                                            className='five columns',
                                            children=[
                                                dcc.Graph(
                                                    id='age-chart',
                                                    figure=fig3,
                                                    config={
                                                        "displayModeBar": False
                                                    },
                                                ),
                                            ]),
                                        html.Div(
                                            className='two columns',
                                            style=dict(marginTop=30),
                                            children=[
                                                html.Div([
                                                    dash_table.DataTable(
                                                        id='table-3',
                                                        columns=[
                                                            dict(id='Summary',
                                                                 name='Summary'
                                                                 ),
                                                            dict(
                                                                id='Value',
                                                                name='Value',
                                                                type='numeric',
                                                                format=Format(
                                                                    precision=2,
                                                                    scheme=Scheme
                                                                    .fixed,
                                                                    trim=Trim.
                                                                    yes))
                                                        ],
                                                        data=df_age_summary.
                                                        to_dict('records'),
                                                        style_as_list_view=True,
                                                        style_cell={
                                                            'padding': '5px'
                                                        },
                                                        style_header={
                                                            'backgroundColor':
                                                            'white',
                                                            'fontWeight':
                                                            'bold'
                                                        })
                                                ],
                                                         style=dict(
                                                             marginBottom=150))
                                            ]),
                                    ])
                            ])
                    ]),
            ]),
        html.Div(  # Stress during the COVID-19
            className='row',
            children=[
                html.Div(
                    className='twelve columns',  # Define the right element
                    children=[
                        dcc.Markdown(
                            '## Stress during the COVID-19 Pandemic by Countries',
                            className='text-center'),
                    ],
                    style=dict(
                        # textAlign='center',
                        # marginTop=35,
                        marginBottom=35),
                ),
                html.Div(dcc.Markdown(f'{paragraph1()}')),
            ]),
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='six columns',  # Define the left element
                    children=[
                        html.Div(
                            children=[
                                html.H6('STRESS levels (Top 10)'),
                            ],
                            style=dict(textAlign='center')
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
                            style=dict(marginTop=-60, )),
                    ],
                ),
                html.Div(
                    className='six columns',  # Define the right element
                    children=[
                        dcc.Markdown('###### STRESS by Countries'),
                        dcc.Markdown('''Visualizing countries ranked
                        with stress levels using the PSS-10 scale.
                        '''),
                        dcc.Markdown(f'{paragraph2()}', )
                        # html.P('''* B&H - Bosnia & Herzegovina''')
                    ],
                    style=dict(marginTop=30)),
            ]),
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='twelve columns',
                    children=[
                        dcc.Markdown(
                            '## Loneliness during the COVID-19 Pandemic by Countries',
                            className='text-center'),
                    ],
                    style=dict(
                        paddingBottom=20,
                        paddingTop=20,
                    )),
                html.Div(dcc.Markdown(f'{paragraph3()}'))
            ]),
        # STATIC ANALYSIS LONELINESS
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='six columns',
                    children=[
                        html.Div(
                            children=[
                                html.H6(
                                    'Perceived LONELINESS levels (Top 10)'),
                            ],
                            style=dict(textAlign='center'),
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
                            style=dict(marginTop=-60, )),
                    ]),
                html.Div(
                    className='six columns',  # Define the right element
                    children=[
                        dcc.Markdown('##### Analysis by Countries'),
                        html.
                        P('''Visualizing countries Loneliness ranked with the results of
                        UCLA short loneliness scale'''),
                        html.P('''*B&H - Bosnia & Herzegovina'''),
                        html.Div(dcc.Markdown(f'{paragraph4()}', ))
                    ]),
            ]),
    ])
