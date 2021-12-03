from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from app import app,dataset
import plotly.express as px
import pandas as pd
import numpy as np

dataset['Date'] = pd.to_datetime(dataset['Date'])
datewise_add = dataset.pivot_table(index=['Date'],aggfunc=np.sum)

def death_cases():
	fig = px.line(datewise_add, x=datewise_add.index, y=datewise_add['Deaths'], title="Trend analysis of Death Cases") 
	return fig


layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Page 2', style = {'textAlign':'center'}),
    dcc.Graph(id = 'line_plot1', figure = death_cases()),
	])


