from dash import html
from dash import dcc
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2


app.layout = html.Div([
    dcc.Location(id='url'),
	dcc.Link('Go to App 1', href='/apps/app1'),
	html.Hr(),
	dcc.Link('Go to App 2', href='/apps/app2'),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return 'This is the home screen'

if __name__ == '__main__':
    app.run_server(debug=True)