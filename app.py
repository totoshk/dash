import dash
import dash_core_components as dcc
import dash_html_components as html
import test_component
import os, sys

import pandas as pd

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

app = dash.Dash()

app.scripts.config.serve_locally = True

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    test_component.ExampleComponent(label="jdhjs"),
    generate_table(df)
])

# colors = {
#     'background': '#111111',
#     'text': '#c2c2c2'
# }

# app.layout = html.Div(children=[
#     html.H1(
#         children='Hello Dash',
#         style={
#             'textAlign': 'center',
#             'color': colors['text']
#         }    
#     ),

#     html.Div(children='''
#         Dash: A web application framework for Python.
#     ''',
#         style = {
#             'textAlign': 'center',
#             'color': colors['text']
#         }
#     ),

#     dcc.Graph(
#         id='example-graph',
#         figure={
#             'data': [
#                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#             ],
#             'layout': {
#                 'title': 'Dash Data Visualization',
#                 'plot_bgcolor': colors['background'],
#                 'paper_bgcolor': colors['background'],
#                 'font': {
#                     'color': colors['text']
#                 }
#             }
#         }
#     )
# ])

if __name__ == '__main__':
    app.run_server(debug=True)