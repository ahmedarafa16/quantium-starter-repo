import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# 1. Load and sort the data
df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by='date')

# 2. Initialize the Dash app
app = dash.Dash(__name__)

# 3. Define the layout with styling
app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'padding': '40px', 'fontFamily': 'Arial, sans-serif'},
                      children=[

                          # Styled Header
                          # Styled Header
                          html.H1(
                              id='header',  # Add this ID here!
                              children='Pink Morsel Sales Visualizer',
                              style={
                                  'textAlign': 'center',
                                  'color': '#2c3e50',
                                  'marginBottom': '30px'
                              }
                          ),

                          # Region Picker Radio Buttons
                          html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
                              html.Label("Filter by Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
                              dcc.RadioItems(
                                  id='region-filter',
                                  options=[
                                      {'label': 'North', 'value': 'north'},
                                      {'label': 'East', 'value': 'east'},
                                      {'label': 'South', 'value': 'south'},
                                      {'label': 'West', 'value': 'west'},
                                      {'label': 'All', 'value': 'all'}
                                  ],
                                  value='all',  # Default value
                                  inline=True,
                                  inputStyle={"margin-left": "20px", "margin-right": "5px"}
                              ),
                          ]),

                          # The Graph
                          dcc.Graph(id='sales-line-chart')
                      ])


# 4. The Callback - This updates the graph whenever the radio button changes
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(region):
    if region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=f'Pink Morsel Sales: {region.capitalize()} Region',
        labels={'sales': 'Total Sales ($)', 'date': 'Date'}
    )

    # Extra styling for the chart itself
    fig.update_layout(
        plot_bgcolor='#ffffff',
        paper_bgcolor='#f9f9f9',
        font_color='#2c3e50'
    )

    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)