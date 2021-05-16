import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash_table


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
layout = html.Div(
    [
    dbc.Container(
        [
        html.Div(
        [
            dbc.Row(dbc.Col(html.Div(
                dcc.Markdown('''
                            ##### SURVEY - Characteristics of the respondants
                            ''', className='text-center'
                            )
                ))),
            dbc.Row(
                dbc.Col(
                    [
                        html.Div(
                            dcc.Markdown(
                                '''
                                ###### Gender of respondents percentage distribution
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
                                style_cell_conditional=[
                                    {
                                        'if': {'column_id': c},
                                        'textAlign': 'left'
                                    } for c in ['Date', 'Region']
                                ],),
                            
                        ], style={'marginTop': 150}),
                             ], width=2),
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
            ),dbc.Row(
                                ##############
                                # EMPLOYMENT #
                                ##############
                dbc.Col(
                    [
                        html.Div(
                            dcc.Markdown(
                                '''
                                ###### Employment Status of respondents perctage distribution
                                ''', className='text-center'
                                )),
                        
                        ], width=12)
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                            dcc.Graph(id='pie-chart-2', figure=fig2)
                            ),
                        ], width=4),
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
                                style_cell_conditional=[
                                    {
                                        'if': {'column_id': c},
                                        'textAlign': 'left'
                                    } for c in ['Date', 'Region']
                                ],),
                            # dcc.Markdown('''
                            # Resopondents were 72.08 % female, 26.89 % Male.
                            # The remaining respondents answered 'other' or did not provide an answer.
                            # ''', style={'marginTop': 150})
                            
                        ], style={'marginTop': 150}),
                             ], width=2),
                    dbc.Col(
                        [
                            html.Div(
                            dcc.Markdown('''
                            Resopondents were 72.08 % female, 26.89 % Male.
                            The remaining respondents answered 'other' or did not provide an answer.
                            ''', style={'marginTop': 150})
                            )
                            
                        ], width={'size':4, 'offset':1}, ),
                            
                    # dbc.Col(html.Div("One of three columns"), width=4)
                ]
            )
            
            
        ]
    )
    ])
    # dbc.Container([
    #     dcc.Markdown(
    #         '''
    #         ##### SURVEY - Characteristics of the respondants
    #         ''', className='text-center'
    #     ),
    #     dbc.Row([
    #         dbc.Row([dbc.Col([
    #                 dcc.Markdown(
    #                     '''
    #                     ###### Gender of respondents percentage distribution
    #                     '''),
    #                 dcc.Markdown(
    #                     '''
    #                     pim pam pum
    #                     '''
    #                 ),
    #                 dcc.Graph(id='pie-chart', figure=fig1)
                    
    #             ]),
                
    #         ])
    #     ])
    # ], fluid=True)
])