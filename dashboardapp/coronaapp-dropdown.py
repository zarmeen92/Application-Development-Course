import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output

app = dash.Dash()   #initialising dash app
dataset = pd.read_csv('corona dataset Pakistan/PK COVID-19-3jun.csv')
dataset['Date'] = pd.to_datetime(dataset['Date'])
datewise_add = dataset.pivot_table(index=['Date'],aggfunc=np.sum)


app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Covid 19 Analysis', style = {'textAlign':'center'}),
    dcc.Dropdown( id = 'dropdown',
        options = [
            {'label':'Recovered Cases', 'value':'Recovered' },
            {'label': 'Death Cases', 'value':'Deaths'}
            
            ],
        value = 'Recovered'),
        dcc.Graph(id = 'line_plot')
	])
@app.callback(Output(component_id='line_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def graph_update(dropdown_value):
	print(dropdown_value)
	fig = px.line(datewise_add, x=datewise_add.index, y=datewise_add['{}'.format(dropdown_value)], title="Trend analysis") 
	return fig  

	
if __name__ == '__main__': 
    app.run_server()