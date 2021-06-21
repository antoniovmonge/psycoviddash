import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from app import server
from apps import app0intro, app1ml, app2viz, app3analytics, app4compare
from psycoviddash.functions import *

import __main__

__main__.edu_func = edu_func
__main__.edu_mom_func = edu_mom_func
__main__.risk_group_func = risk_group_func
__main__.expat_func = expat_func

app.layout = html.Div(
    children=[
        html.Div(
            className="header",
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H1(
                                    className="header-title",
                                    children="PsyCovid Analytics",
                                ),
                                html.P(
                                    className="header-description",
                                    children='THE PSYCHOLOGICAL INPACT DURING COVID-19 OUTBREAK',
                                ),
                            ],width=6
                        ),
                        dbc.Col(
                            [
                                dcc.Markdown(
                                    '''
                                    Project created by:    
                                    [Antonio Vilchez Monge,](https://www.linkedin.com/in/antonio-v-monge/)
                                    [Verónica Delgado Benito,](https://www.linkedin.com/in/veronica-delgadobenito/)
                                    [Shruthi L.P,](https://www.linkedin.com/in/shruthilp/)
                                    [Wojciech Gutkiewicz](https://www.linkedin.com/in/gutkiewicz/)
                                    ''',
                                    style=dict(
                                        textAlign='right',
                                        paddingRight=80,
                                        paddingTop=15,
                                        color='white',
                                    ),
                                )
                            ], width=6
                        ),
                    ]
                ),


            ],
            style=dict(
                position= 'sticky',
                top= 0,
            )
        ),
        html.Div(
            [
                dcc.Tabs(
                    id='tabs',
                    value='Tab One',
                    parent_className='custom-tabs',
                    className='custom-tabs-container',
                    children=[
                        dcc.Tab(
                            label='Home',
                            value='tab-0',
                            className='custom-tab',
                            selected_className='custom-tab--selected'
                        ),
                        dcc.Tab(
                            label='Predictions / Simulation',
                            value='tab-1',
                            className='custom-tab',
                            selected_className='custom-tab--selected'
                        ),
                        dcc.Tab(
                            label='Survey Analysis',
                            value='tab-2',
                            className='custom-tab',
                            selected_className='custom-tab--selected'
                        ),
                        dcc.Tab(
                            label='Analytics',
                            value='tab-3',
                            className='custom-tab',
                            selected_className='custom-tab--selected'
                        ),
                        dcc.Tab(
                            label='Countries Comparison',
                            value='tab-4',
                            className='custom-tab',
                            selected_className='custom-tab--selected'
                        ),
                    ]
                ),
                # html.Div(id='tabs-content')
            ],
            style=dict(
                position= 'sticky',
                top= 85,
                zIndex= 9999,
            )
        ),
        html.Div(id='page-content', children=[])

        #################
        # OLD SELECTORS #
        #################
        # html.Div(
        #     className='text-center text-black-50, mb-4',
        #     children=[

        #         dcc.Link('Intro |', href='/apps/app0intro'),
        #         dcc.Link(' Machine Learning |', href='/apps/app1ml'),
        #         dcc.Link(' Survey Visualization |', href='/apps/app2viz'),
        #         dcc.Link(' Analysis by Country |', href='/apps/app3country'),
        #     ],
        # ),
        # dcc.Location(id='url', refresh=False),

    ],


)
#callback to control the tab content
@app.callback(Output('page-content', 'children'),[Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-0':
        return app0intro.layout
    elif tab == 'tab-1':
        return app1ml.layout
    elif tab == 'tab-2':
        return app2viz.layout
    elif tab == 'tab-3':
        return app3analytics.layout
    elif tab == 'tab-4':
        return app4compare.layout
    else:
        return app0intro.layout # CHANGE WITH app0intro.layout !!

################
# OLD CALLBACK #
################
# @app.callback(Output(component_id='page-content', component_property='children'),
#               Input(component_id='url', component_property='pathname'))

# def display_page(pathname):
#     if pathname == '/apps/app0intro':
#         return app0intro.layout
#     elif pathname == '/apps/app1ml':
#         return app1ml.layout
#     elif pathname == '/apps/app2viz':
#         return app2viz.layout
#     elif pathname == '/apps/app3country':
#         return app3analytics.layout
#     else:
#         return app0intro.layout

if __name__ == '__main__':
    app.run_server(debug=True)
