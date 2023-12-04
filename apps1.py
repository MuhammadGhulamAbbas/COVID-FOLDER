from app import data
import pandas as pd
from plotly  import express as px
from dash import dcc,html
import numpy as np
import pandas as pd

data['Date']=pd.to_datetime(data['Date'],errors='coerce')
df=data.pivot_table(index=data.index,aggfunc=np.sum)
fig1 = px.line(df,x=df.index,  y=df['Deaths'],title="Death Analysis")

layout=([
    html.H1("Page-1"),
    html.Br(),
    dcc.Graph(id='lin_plot',figure=fig1)
    ])

