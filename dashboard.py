import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# # DataFrame
# data = {
#     'County': ['ALAMEDA', 'ALAMEDA', 'ALAMEDA', 'ALAMEDA', 'ALAMEDA', 'YUBA', 'YUBA', 'YUBA', 'YUBA', 'YUBA'],
#     'Sector': ['Non-Residential', 'Residential', 'Total', 'Non-Residential', 'Residential', 'Non-Residential', 'Residential', 'Total', 'Non-Residential', 'Residential'],
#     'Yearly Data': [7109.299895, 2498.265626, 9607.565521, 6809.573768, 2515.20997, 315.822249, 260.500675, 576.322924, 315.822249, 260.500675],
#     'Timestamp': ['1990-01-01', '1990-01-01', '1990-01-01', '1991-01-01', '1991-01-01', '2020-01-01', '2020-01-01', '2020-01-01', '2021-01-01', '2021-01-01']
# }
# Read the Excel file
df = pd.read_excel('Datasets/ElectricityByCounty.xlsx')

# Reshape the DataFrame
df = df.melt(id_vars=['County', 'Sector'],
             var_name='Timestamp', value_name='Yearly Data')

# Convert the "Timestamp" column to datetime format representing the year
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y')

# Sort the DataFrame by County and Timestamp
df = df.sort_values(['County', 'Timestamp'])





# Create the Plotly Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Electricity Usage Dashboard"),
    html.Div([
        dcc.Dropdown(
            id='county-dropdown',
            options=[{'label': county, 'value': county} for county in df['County'].unique()],
            value=df['County'].unique()[0]
        ),
        dcc.Dropdown(
            id='sector-dropdown',
            options=[{'label': sector, 'value': sector} for sector in df['Sector'].unique()],
            value=df['Sector'].unique()[0]
        ),
    ], style={'width': '50%', 'margin': 'auto', 'padding': '10px'}),
    dcc.Graph(id='usage-graph')
])

# Define the callback functions
@app.callback(
    dash.dependencies.Output('usage-graph', 'figure'),
    [dash.dependencies.Input('county-dropdown', 'value'),
     dash.dependencies.Input('sector-dropdown', 'value')]
)
def update_graph(county, sector):
    filtered_df = df[(df['County'] == county) & (df['Sector'] == sector)]
    fig = px.line(filtered_df, x='Timestamp', y='Yearly Data',markers = 'lines+markers', title=f"Electricity Usage for {county} - {sector}")
    fig.update_layout(xaxis_title='Timestamp', yaxis_title='Yearly Data')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
