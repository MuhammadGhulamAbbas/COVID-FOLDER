from dash import dcc, html
from dash.dependencies import Input, Output
from app import data, app
from apps import apps1,apps2


app.layout = html.Div([
    html.H1("Welcome to COVID 19 Analytics Dashboard"),
    html.Hr(),
    html.H2("Trend Analysis"),
    html.Br(),
    dcc.Location(id='url'),
    dcc.Link("Go to App1", href='/apps/apps1'),
    html.Br(),
    dcc.Link("Go to App2", href="/apps/apps2"),
    html.Div(id='Page_content')
])

@app.callback(Output('Page_content','children'),
                     Input('url','pathname'))
def display_page_content(path):
    if path=='/apps/apps1':
        return apps1.layout
    elif  path=='/apps/apps2':
        return apps2.layout
    else:
        return ("This is your homepage")
    
       

    


if __name__ == '__main__':
    app.run(debug=True)




