import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server

from apps import app0intro, app1ml, app2viz, app3country


app.layout = html.Div([
    html.Div([
        dcc.Link('Intro |', href='/apps/app0intro'),
        dcc.Link(' Machine Learning |', href='/apps/app1ml'),
        dcc.Link(' Survey Visualization |', href='/apps/app2viz'),
        dcc.Link(' Analysis by Country |', href='/apps/app3country'),
    ], className='text-center text-black-50, mb-4'),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])


@app.callback(Output(component_id='page-content', component_property='children'),
              Input(component_id='url', component_property='pathname'))

def display_page(pathname):
    if pathname == '/apps/app0intro':
        return app0intro.layout
    elif pathname == '/apps/app1ml':
        return app1ml.layout
    elif pathname == '/apps/app2viz':
        return app2viz.layout
    elif pathname == '/apps/app3country':
        return app3country.layout
    else:
        return app0intro.layout

if __name__ == '__main__':
    app.run_server(debug=True)
    