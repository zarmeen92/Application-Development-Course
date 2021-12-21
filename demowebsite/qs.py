import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Change the Input Value"),
    dcc.Input(id='my-input', value='initial value', type='text'),
    html.Br(),
    html.Div(id='my-output')
])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return 'Output: ' + input_value


if __name__ == '__main__':
    app.run_server(debug=True)