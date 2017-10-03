import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import flask
import os

data_matrix = [['Anna', 'United States', 12],
               ['Peter', 'Canada', 22],
               ['Anna', 'United States', 30],
               ['John', 'Canada', 18],
               ['John', 'United States', 30],
               ['John', 'Canada', 24]]

df = pd.DataFrame(data_matrix)

def generate_table(dataframe, max_rows=10):
    return html.Table(
        [html.Tr([
            html.Th('Name'),
            html.Th('Country'),
            html.Th('Age')
        ])] +
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

app = dash.Dash()

app.layout = html.Div ([
    html.H1 (
        children='Hello Dash'
    ),
    html.Div (className = 'header', children = [
        html.Div (
            className = 'header-search',
            children = [
                html.P (
                    className = 'header-search__title',
                    children = 'Search:'),
                dcc.Input (
                    className = 'header-search__input',
                    id='inputField',
                    placeholder='Search by name',
                    type='text'
                )
            ]
        ),
        html.Div (
            className = 'header-filter',
            children = dcc.Dropdown (
                className = 'header-filter__options',
                id='filterOptions',
                options = [
                    {'label': 'Show All', 'value': 'Show All'},
                    {'label': 'United States', 'value': 'United States'},
                    {'label': 'Canada', 'value': 'Canada'}
                ],
                value='Show All'
            )
        )
    ]),
    html.Div (
        id='mainTable',
        children = generate_table(df)
    )
])

css_directory = os.getcwd()
stylesheets = ['stylesheet.css']
static_css_route = '/static/'

@app.server.route('{}<stylesheet>'.format(static_css_route))
def serve_stylesheet(stylesheet):
    if stylesheet not in stylesheets:
        raise Exception(
            '"{}" is excluded from the allowed static files'.format(
                stylesheet
            )
        )
    return flask.send_from_directory(css_directory, stylesheet)


for stylesheet in stylesheets:
    app.css.append_css({"external_url": "/static/{}".format(stylesheet)})


def searchSubstr(table, value):
    filtered_table = []
    for row in table:
        for item in row:
          if str(item).find(str(value)) != -1 and str(item).find(str(value)) != -1:
            filtered_table.append(row)
            print(row)
            break
    return filtered_table

def filterTable(searchValue, filterOption):
    if searchValue != None and searchValue != '' and filterOption != 'Show All':
        new_table = searchSubstr(searchSubstr(data_matrix, searchValue), filterOption)
    elif searchValue != None and searchValue != '':
        new_table = searchSubstr(data_matrix, searchValue)
    elif filterOption != 'Show All':
         new_table = searchSubstr(data_matrix, filterOption)
    else:
        new_table = data_matrix
    res = pd.DataFrame(new_table)
    return(res)

@app.callback(
    Output('mainTable', 'children'),
    [Input('inputField', 'value'),
    Input('filterOptions', 'value')]
)
def filterValues(input_val, filter_val):
    return generate_table(filterTable(input_val, filter_val))


if __name__ == '__main__':
    app.run_server()