import dash
from dash import dcc, html, Input, Output, State
from generative_ai_site.models.code_completion import get_code_completion
from generative_ai_site.models.stable_diffusion import generate_image

import dash_bootstrap_components as dbc

# Choose a dark theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Code Completion', value='tab-1'),
        dcc.Tab(label='Stable Diffusion Image Generation', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Code Completion'),
            dcc.Textarea(id='code-input', style={'width': '100%', 'height': 200}),
            html.Button('Complete Code', id='complete-code-btn'),
            html.Div(id='code-output')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Image Generation with Stable Diffusion'),
            dcc.Input(id='image-prompt', type='text', placeholder='Enter prompt for image generation'),
            html.Button('Generate Image', id='generate-image-btn'),
            # Update here: Add an html.Img element for displaying the generated image
            html.Img(id='generated-image', style={'max-width': '100%', 'height': 'auto'})
        ])


@app.callback(Output('code-output', 'children'),
              Input('complete-code-btn', 'n_clicks'),
              State('code-input', 'value'))
def complete_code(n_clicks, code_input):
    if n_clicks and code_input:
        completed_code = get_code_completion(code_input)
        print('Completing Code')
        return dcc.Textarea(value=completed_code, style={'width': '100%', 'height': 200})
    return dcc.Textarea(value="Enter code prompt above to get output...", style={'width': '100%', 'height': 200})

@app.callback(
    Output('generated-image', 'src'),
    Input('generate-image-btn', 'n_clicks'),
    State('image-prompt', 'value')
)
def update_image_src(n_clicks, prompt):
    if n_clicks and prompt:
        src_data = generate_image(prompt)
        return src_data
    return None

if __name__ == '__main__':
    app.run_server(debug=True)

