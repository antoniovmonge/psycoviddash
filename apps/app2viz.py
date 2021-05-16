import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash_table
import numpy as np


from app import app

df = pd.read_csv('cleaned_data_040321.csv',index_col=0)
df = df.replace({'Dem_gender':'Other/would rather not say'}, 'Other')

# GENDER PIE CHART FIG 1
color_palette_list = ['#CDF1AE', '#90DACC', '#F7E9D1', '#F4D2B5',
'#EAB7B7', '#B89ACF']
# values = list(df['Dem_gender'].value_counts(normalize=True))
# names = list(df['Dem_gender'].value_counts().index)
fig1 = px.pie(df,
              values=list(df['Dem_gender'].value_counts(normalize=True)),
              names=list(df['Dem_gender'].value_counts().index))
fig1.update_traces(textposition='outside',
                   textinfo='percent+label',
                marker=dict(colors=color_palette_list))
fig1.update_layout(showlegend=False)

# EMPLOYMENT PIE CHART
fig2 = px.pie(df,
              values=list(df['Dem_employment'].value_counts(normalize=True)),
              names=list(df['Dem_employment'].value_counts().index))
fig2.update_traces(textposition='inside',
                   textinfo='percent+label',
                marker=dict(colors=color_palette_list))
fig2.update_layout(showlegend=False)

# TABLE GENDER
# df_gender = pd.DataFrame(
#     (df['Dem_gender'].value_counts(normalize=True)))
# df_gender.columns = ['%']

df_gender = df[['Dem_gender']].copy()
df_gender = pd.DataFrame(
            (df['Dem_gender'].value_counts(normalize=True).round(2))).reset_index()
df_gender.columns = ['Gender', '%']
df_gender = df_gender.replace({'Gender':'Other/would rather not say'},'Other')

df_employment = df[['Dem_employment']].copy()
df_employment = pd.DataFrame(
    (df['Dem_employment'].value_counts(normalize=True).round(2))).reset_index()
df_employment.columns = ['Empl. Status', '%']

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
    [
    dbc.Container(
        [
        html.Div(

            [
                dbc.Row(dbc.Col(html.Div(
                    dcc.Markdown('''
                                #### SURVEY - Characteristics of the respondants
                                ''', className='text-center'
                                )
                    ))),
                # SECTION 1 (GENDER)
                dbc.Row(
                    dbc.Col(
                        [
                            html.Div(
                                dcc.Markdown(
                                    '''
                                    ##### Gender of respondents percentage distribution
                                    ''', className='text-center'
                                    )),
                            
                            ], width=12)
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                dcc.Graph(id='pie-chart', figure=fig1)
                                ),
                            ], width=4),
                        dbc.Col([
                            html.Div([
                                dash_table.DataTable(
                                    id='table',
                                    columns=[{"name": i, "id": i} for i in df_gender.columns],
                                    data=df_gender.to_dict('records'),
                                    style_as_list_view=True,
                                    style_cell={'padding': '5px'},
                                    style_header={
                                        'backgroundColor': 'white',
                                        'fontWeight': 'bold'
                                    },
                                ),
                                
                            ],
                            style={'marginTop': 150}
                            ),
                        ], width=2
                        ),
                        dbc.Col(
                            [
                                html.Div(
                                dcc.Markdown('''
                                Resopondents were 72.08 % female, 26.89 % Male. The remaining respondents answered 'other' or did not provide an answer.
                                ''', style={'marginTop': 150})
                                )
                                
                            ], width={'size':5, 'offset':1}, ),
                                
                        # dbc.Col(html.Div("One of three columns"), width=4)
                    ]
                ),
                        
                # SECTION 2 (EMPLOYMENT)
                # Title
                dbc.Row(             
                    dbc.Col(
                        [
                            html.Div(
                                dcc.Markdown(
                                    '''
                                    ##### Employment Status of respondents percentage distribution
                                    ''', className='text-center'
                                    )),
                            
                            ], width=12)
                ),
                # Chart, Table and Text (3 Columns)
                dbc.Row(
                    [
                        # COL LEFT
                        dbc.Col(
                            [
                                html.Div(
                                dcc.Graph(id='pie-chart-2', figure=fig2)
                                ),
                            ], 
                            width=4),
                        # COL CENTER
                        dbc.Col([
                            html.Div([
                                dash_table.DataTable(
                                    id='table-2',
                                    columns=[{"name": i, "id": i} for i in df_employment.columns],
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
                            style={'marginTop': 150}
                            ),
                        ], width=2
                        ),
                        # COL RIGHT
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        dcc.Markdown('''
                                        Resopondents were 72.08 % female, 26.89 % Male. The remaining respondents answered 'other' or did not provide an answer.
                                        ''', style={'marginTop': 150})
                                    ]
                                )
                                
                            ], width={'size':5, 'offset':1}),
                                
                        # dbc.Col(html.Div("One of three columns"), width=4)
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
                                ], style={'marginTop': 100}
                            ),
                            
                            ], width=12)
                ),
                # CHART
                dbc.Row(
                    [
                        dbc.Col([
                            html.Div(
                                dcc.Graph(id='age-chart', figure=fig3)
                                ),
                        ], width=6,
                        ),
                        dbc.Col([
                            html.Div(
                                [
                                    dash_table.DataTable(
                                    id='table-3',
                                    columns=[{"name": i, "id": i} for i in df_age_summary.columns],
                                    data=df_age_summary.to_dict('records'),
                                    style_as_list_view=True,
                                    style_cell={'padding': '5px'},
                                    style_header={
                                        'backgroundColor': 'white',
                                        'fontWeight': 'bold'
                                    }
                                    )
                                ], style={'marginTop': 100, 'marginBottom': 200}
                            )    
                        ])
                    ]
                )
            ])
                    
                ]
            )
        ]
    )
    

