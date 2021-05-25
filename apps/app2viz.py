import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash_table
from dash_table.Format import Format, Scheme, Trim
import numpy as np


from app import app

# url='s3://psycovid/cleaned_data_040321.csv'
# df = pd.read_csv(url ,index_col=0)
df = pd.read_csv('raw_data/cleaned_data_040321.csv',index_col=0)
df = df.replace({'Dem_gender':'Other/would rather not say'}, 'Other')

# GENDER PIE CHART FIG 1
color_palette_list = ['#CDF1AE', '#90DACC', '#F7E9D1', '#F4D2B5',
'#EAB7B7', '#B89ACF']
# values = list(df['Dem_gender'].value_counts(normalize=True))
# names = list(df['Dem_gender'].value_counts().index)
fig1 = px.pie(
    df,
    values=list(df['Dem_gender'].value_counts(normalize=True)),
    names=list(df['Dem_gender'].value_counts().index)
)
fig1.update_traces(
    textposition='outside',
    textinfo='percent+label',
    marker=dict(colors=color_palette_list)
)
fig1.update_layout(
    showlegend=False,
    margin=dict(
            l=0,
            r=0,
            b=0,
            t=0,
            pad=0
        )
)

# EMPLOYMENT PIE CHART
fig2 = px.pie(df,
              values=list(df['Dem_employment'].value_counts(normalize=True)),
              names=list(df['Dem_employment'].value_counts().index))
fig2.update_traces(textposition='inside',
                   textinfo='percent+label',
                marker=dict(colors=color_palette_list))
fig2.update_layout(
    showlegend=False,
    margin=dict(
            l=30,
            r=30,
            b=0,
            t=0,
            pad=4
        )
)

# TABLE GENDER
# df_gender = pd.DataFrame(
#     (df['Dem_gender'].value_counts(normalize=True)))
# df_gender.columns = ['%']

# GENDER TABLE
df_gender = df[['Dem_gender']].copy()
df_gender = pd.DataFrame(
            (df['Dem_gender'].value_counts(normalize=True).round(3)*100)).reset_index()
df_gender.columns = ['Gender', '%']
df_gender = df_gender.replace({'Gender':'Other/would rather not say'},'Other')
# df_gender['%']=pd.Series(["{0:.2f}".format(val * 100) for val in df_gender['%']], index = df_gender.index)

# EMPLOYMENT TABLE
df_employment = df[['Dem_employment']].copy()
df_employment = pd.DataFrame(
    (df['Dem_employment'].value_counts(normalize=True).round(3)*100)).reset_index()
df_employment.columns = ['Empl. Status', '%']
# df_employment['%'] = (df_employment['%'] / df_employment['%'].sum() * 100)

# AGE CHART
# counts, bins = np.histogram(df.Dem_age, bins=range(18, 115))
# bins = (0.5 * bins[:-1] + bins[1:])
data_age = df.Dem_age.value_counts()
fig3 = px.bar(data_age, labels={'index': 'Age', 'value': 'Count'}, template="simple_white")
fig3.update_traces(marker=dict(color=color_palette_list[1]))
fig3.update_layout(height=350, showlegend=False)
fig3.update_yaxes(showgrid=True)

# AGE TABLE
d = {'Summary':['Mean','Median','Mode','Min','Max'],'Value':[df[['Dem_age']].mean()[0].round(2), df[['Dem_age']].median()[0], df['Dem_age'].mode()[0], df[['Dem_age']].min()[0], df[['Dem_age']].max()[0]]}
df_age_summary = pd.DataFrame(data=d)

# LAYOUT
layout = html.Div(
    className='main-container',
    children=[
        dbc.Container(
            [
                html.Div(

                    [
                        dbc.Row(
                            dbc.Col(
                                html.Div(

                                    dcc.Markdown('''
                                                ### SURVEY - Characteristics of the respondants
                                                ''', className='text-center'
                                                )
                                )
                            )
                        ), 
                        # SECTION 1 (GENDER)
                        dbc.Row(
                            dbc.Col(
                                [
                                    html.Div(
                                        [
                                            dcc.Markdown(
                                                '''
                                                ##### Gender of respondents percentage distribution
                                                ''', className='text-center'
                                            )
                                        ], style={'marginTop': 50}
                                    ),
                                    
                                ],
                                width=12
                            )
                        ), 
                        # SECTION 1 (GENDER) COLUMNS
                        dbc.Row(
                            [
                                # SECTION 1 (GENDER) CHART
                                dbc.Col(
                                    [
                                        html.Div(
                                        dcc.Graph(id='pie-chart', figure=fig1)
                                        ),
                                    ], width=4),
                                # SECTION 1 (GENDER) TABLE
                                dbc.Col(
                                    [
                                        html.Div(
                                            [

                                                dash_table.DataTable(
                                                    id='table',
                                                    columns=[
                                                        dict(id= 'Gender', name='Gender'),
                                                        dict(id='%', name='%', type='numeric', format=Format(precision=2, scheme=Scheme.fixed))
                                                    ],
                                                    data=df_gender.to_dict('records'),
                                                    style_as_list_view=True,
                                                    style_cell={'padding': '5px'},
                                                    style_header={
                                                        'backgroundColor': 'white',
                                                        'fontWeight': 'bold'
                                                    },
                                                ),
                                            
                                            ],
                                            style={'marginTop': 125}
                                        ),
                                    ],
                                    width={'size':2, 'offset':1}
                                ),
                                # SECTION 1 (GENDER) TEXT
                                dbc.Col(
                                    [
                                        html.Div(

                                            dcc.Markdown(f'''
                                            Resopondents were {72.08} % female, 26.89 % Male. The remaining respondents answered 'other' or did not provide an answer.
                                            ''', style={'marginTop': 125}
                                            )
                                        )
                                        
                                    ], 
                                    width={'size':4, 'offset':1}, 
                                ),
                                        
                                # dbc.Col(html.Div("One of three columns"), width=4)
                            ]
                        ),
                                
                        # SECTION 2 (EMPLOYMENT)
                        # Title
                        dbc.Row(             
                            dbc.Col(
                                [
                                    html.Div(
                                        [
                                        dcc.Markdown(
                                            '''
                                            ##### Employment Status of respondents percentage distribution
                                            ''', className='text-center'
                                            )
                                        ], style={'marginTop': 100, 'marginBottom':50}
                                    ),
                                        
                                ],
                                width=12)
                        ),
                        # SECTION 2 (EMPLOYMENT) Chart, Table and Text (3 Columns)
                        dbc.Row(
                            [
                                # COL LEFT (cHART)
                                dbc.Col(
                                    [
                                        html.Div(
                                            dcc.Graph(id='pie-chart-2', figure=fig2)
                                        ),
                                    ], 
                                    width=4),
                                # COL CENTER (TABLE)
                                dbc.Col(
                                    [

                                        html.Div(
                                            [
                                                dash_table.DataTable(
                                                    id='table-2',
                                                    columns=[
                                                        dict(id= 'Empl. Status', name='Employment Status'),
                                                        dict(id='%', name='%', type='numeric', format=Format(precision=2, scheme=Scheme.fixed))
                                                    ],
                                                    data=df_employment.to_dict('records'),
                                                    style_as_list_view=True,
                                                    style_cell={'padding': '5px'},
                                                    style_header={
                                                        'backgroundColor': 'white',
                                                        'fontWeight': 'bold'
                                                    },
                                                ),
                                        # dcc.Markdown('''
                                        # Resopondents were 72.08 % female, 26.89 % Male.
                                        # The remaining respondents answered 'other' or did not provide an answer.
                                        # ''', style={'marginTop': 150})
                                        
                                            ],
                                            style={'marginTop': 125}
                                        ),
                                    ],
                                    width={'size':3, 'offset':1}
                                ),
                                # COL RIGHT (TEXT)

                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                dcc.Markdown(
                                                    f'''
                                                    The majority of the respondents ({(float(df_employment.iloc[0]['%']) + float(df_employment.iloc[2]['%']) + 
                                                    float(df_employment.iloc[3]['%'])) }%) 
                                                    were in full-time, part-time or self-employed, ({(float(df_employment.iloc[4]['%']) + float(df_employment.iloc[5]['%']))}%) 
                                                    were either unemployed or retired, {float(df_employment.iloc[1]['%'])}% were students.
                                                    ''', style={'marginTop': 125}
                                                )
                                            ]
                                        )
                                        
                                    ], width={'size':3, 'offset':1}
                                ),
                            ]
                        ),
                        #######
                        # AGE #
                        #######

                        # SECTION TITLE 3
                        dbc.Row(
                            dbc.Col(
                                [
                                    html.Div(
                                        [
                                            dcc.Markdown(
                                                '''
                                                ##### Age of respondents 
                                                ''', className='text-center'
                                                )
                                        ], style={'marginTop': 200, 'marginBottom': 100}
                                    ),
                                    
                                ], width=12
                            )
                        ),
                        # CHART
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            dcc.Graph(id='age-chart', figure=fig3)
                                            ),
                                    ], width=5,
                                ),

                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                dash_table.DataTable(
                                                id='table-3',
                                                columns=[
                                                    dict(id= 'Summary', name='Summary'),
                                                    dict(id='Value', name='Value', type='numeric', format=Format(precision=2, scheme=Scheme.fixed, trim=Trim.yes))
                                                ],
                                                data=df_age_summary.to_dict('records'),
                                                style_as_list_view=True,
                                                style_cell={'padding': '5px'},
                                                style_header={
                                                    'backgroundColor': 'white',
                                                    'fontWeight': 'bold'
                                                }
                                                )
                                            ], style={'marginTop': 75, 'marginBottom': 200}
                                        )    
                                    ]
                                ),

                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                dcc.Markdown(
                                                    f'''
                                                    The age of the respondents ranged from {df[['Dem_age']].min()[0]} to {df[['Dem_age']].max()[0]}, with a median age of {int(df[['Dem_age']].median()[0])}.
                                                    The age that appears more offen is {df['Dem_age'].mode()[0]}.
                                                    ''',
                                                    style={'marginTop': 75}
                                                )
                                            ]
                                        )
                                    ], width={'size':4, 'offset':1}
                                )
                            ]
                        )
                    ]
                )     
            ]
        )
    ]
)
    

