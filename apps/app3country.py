import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import app

df = pd.read_csv('cleaned_data_040321.csv',index_col=0)
# PREPARE DF
df_stress = df.groupby(['Country']).mean().reset_index()
df_stress_country = df_stress[['PSS10_avg', 'Country']].sort_values(
    by='PSS10_avg', ascending=True)

# PLOTLY BAR CHART
fig = px.bar(
    df_stress_country[-10:],
    y='Country',
    x='PSS10_avg',
    text='Country',
    height=400,
    title='Top 10 Countries with higher degrees of stress',
    labels={'PSS10_avg': 'Stress Level'}
)
fig.update_traces(
    marker_color='rgb(158,202,225)',
    width=0.5,
    # marker_line_color='rgb(255, 0, 116)',
    # marker_line_width=1.5,
    opacity=0.6,
    textposition='outside'
)
fig.update_layout(
    uniformtext_minsize=1,
    uniformtext_mode='hide',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)'
)        
fig.update_xaxes(
    range=[1, 5],
    showgrid=True,
    gridcolor='rgba(234, 234, 234, 0.6)'
)
# My personal trick to separate the y axis
fig.update_yaxes(
    ticklabelposition='outside left',
    ticks="outside", tickwidth=2, tickcolor='white', ticklen=5
)


layout = html.Div(
    children=[
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='four columns div-user-controls', # Define the left element
                    children=[
                        html.H2('Analysis by Countries'),
                        html.P('''Visualising countries ranked ''')
                    ]
                ),
                html.Div(
                    className='eight columns div-for-charts', # Define the right element
                    children=[
                        dcc.Graph(id='line-fig', figure=fig)
                    ]
                )
            ]
        )
    ]
)
# layout = html.Div(
#     [
#         dbc.Container(
#             [
#                 html.Div(
#                     [
#                         dbc.Row(
#                             [
#                                 html.H3('Analysis by Countries'),
                                
#                             ]
#                         ),
#                         dbc.Row(
#                             [
#                                 dcc.Dropdown(
#                                     id='app-3-dropdown',
#                                     options=[
#                                         {'label': 'App 3 - {}'.format(i), 'value': i} for i in [
#                                             'NYC', 'MTL', 'LA'
#                                         ]
#                                     ]
#                                 ),
                                
#                             ]
#                         ),
#                         dbc.Row(
#                             [
#                                 html.Div(id='app-3-display-value')

#                             ]
#                         )
#                     ]
#                 )
#             ]
#         )
        
#     ]
# )


@app.callback(
    Output('app-3-display-value', 'children'),
    Input('app-3-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)
