import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from dash import Dash, html, dcc,  Input, Output
df = pd.read_csv('avocado-updated-2020.csv')

#print(df.head())

#initialize dash app
#backend works on a flask app
app = Dash()

# creating a dropdown menu
dropdown_Menu = dcc.Dropdown(
    options=df['geography'].unique(),
    value='New York'
)

#create a bar plot of number of average price per geography
fig = px.bar(df, x = 'geography',y='average_price', color='type', barmode='group')

fig_2 = px.pie(data_frame=df,names=df['type'].unique(), values=df['type'].value_counts())

# Establishing layout. This is supported by JavaScript in the backend which helps making HTML page
app.layout = html.Div(
    children=[
        html.H2(children='Avocado Price Dashboard'),
        html.Div(children='Sample for Nancy'),
        dropdown_Menu,
        dcc.Graph(id='price_graph'),
        dcc.Graph(id = 'bar_plot', figure=fig),
        dcc.Graph(id = 'pie_chart', figure=fig_2)

    ]
)

#python magic callback function will enable interaction to the dropdown menu
@app.callback(
    Output(component_id='price_graph', component_property='figure'),
    Input(component_id=dropdown_Menu, component_property='value')
)
def update_plot(selected_graph):
    temp_df = df[df['geography'] == selected_graph ]
    line_plot = px.line(
        temp_df,
        x = 'date',
        y = 'average_price',
        color = 'type',
        title = f'Avocado Price in {selected_graph}'
    )

    return line_plot




if __name__ == "__main__":
    app.run_server()



