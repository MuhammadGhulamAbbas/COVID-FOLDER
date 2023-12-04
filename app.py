import dash
import pandas as pd
app=dash.Dash()
data=pd.read_csv('dataset/COVID.csv')
