from app import data
import pandas as pd
from plotly  import express as px
from dash import dcc,html
import numpy as np
import pandas as pd


data['Date']=pd.to_datetime(data['Date'],errors='coerce')
df=data.pivot_table(index=data.index,aggfunc=np.sum)
fig2 = px.scatter(df,x=df.index,  y=df['Cases'],title="Case Analysis")

layout=([
    html.H1("Page-2"),
    html.Br(),
    dcc.Graph(id = 'scatter_plot',figure=fig2)
    ])

