import dash
import pandas as pd
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server
dataset = pd.read_csv('corona dataset Pakistan/PK COVID-19-3jun.csv')
