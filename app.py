import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# 1. Load the data we formatted in the last step
df = pd.read_csv('formatted_data.csv')

# The assignment asks to sort the data by date
df = df.sort_values(by='date')

# 2. Initialize the Dash app
app = dash.Dash(__name__)

# 3. Create the line chart using Plotly Express
# We are plotting 'date' on the x-axis and 'sales' on the y-axis
fig = px.line(df, x='date', y='sales', title='Pink Morsel Sales Over Time')

# 4. Define the layout of the app
app.layout = html.Div(children=[
    # The Header
    html.H1(
        children='Pink Morsel Sales Visualizer',
        style={'textAlign': 'center'}
    ),

    # The Line Chart
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Run the app!
if __name__ == '__main__':
    app.run(debug=True)