import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {
    'font-color': '#000080',
    'heading-color': '#000066',
    'border-color': '#0000b3'
}

app.layout = html.Div ([
    html.H1 (
        children='Hello Dash',
        style={
            'color': colors['heading-color']
        }
    ),
    dcc.Input (
        id='inputField',
        placeholder='Enter your name here',
        type='text',
        style={
            'border': '1px solid ',
            'border-color': colors['border-color']
        }
    ),
    html.Div (
        id='resultField',
        style={
            'color': colors['font-color']
        },
        children = [
            'Your name is: ',
            html.Span(id='resultName', style={'fontWeight': 'bold'})
        ]
    )  
])

@app.callback(
    Output(component_id='resultName', component_property='children'),
    [Input(component_id='inputField', component_property='value')]
)

def update_resultField(input_val):
    if input_val is None or input_val == '':
        val = 'You forgot to enter name'
    else:
        val = input_val
    return '{}'.format(val)

if __name__ == '__main__':
    app.run_server()