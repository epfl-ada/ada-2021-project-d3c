from dash import dcc
from dash import html

from app import app 
import group_app, line_app

app.layout = html.Div(children=[
    html.Div(children=group_app.layout()),
    html.Div(children=line_app.layout())
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)