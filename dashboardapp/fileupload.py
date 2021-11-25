import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import base64
import os
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Upload(id='upload-data',children=html.Button('Upload File')),
    html.Hr(),
	html.Div(id='output-data-upload')
])
def save_file(name, content):
	"""Decode and store a file uploaded with Plotly Dash."""
	data = content.encode("utf8").split(b";base64,")[1]
	with open(name, "wb") as fp:
		fp.write(base64.decodebytes(data))
	f = open(name,"r")
	return f.read()


@app.callback(Output('output-data-upload', 'children'),
              Input("upload-data", "filename"),
			  Input("upload-data", "contents")
             )
def read_output(fname,content):
	print(fname)
	print(content)
	return save_file(fname,content)
	
        


if __name__ == '__main__':
    app.run_server()
