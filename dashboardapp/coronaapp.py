import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd
import numpy as np

app = dash.Dash(__name__)   #initialising dash app
dataset = pd.read_csv('corona dataset Pakistan/PK COVID-19-3jun.csv')
dataset['Date'] = pd.to_datetime(dataset['Date'])
datewise_add = dataset.pivot_table(index=['Date'],aggfunc=np.sum)

def recovered_cases():
	fig = px.line(datewise_add, x=datewise_add.index, y=datewise_add['Recovered'], title="Trend analysis of Recovered Cases") 
	return fig


app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Covid 19 Analysis', style = {'textAlign':'center'}),
    dcc.Graph(id = 'line_plot1', figure = recovered_cases()),
	])
	
if __name__ == '__main__': 
    app.run_server()