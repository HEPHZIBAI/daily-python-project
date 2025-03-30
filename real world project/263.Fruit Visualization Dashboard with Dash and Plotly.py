'''
Project Brief
    For this project, we will create an interactive web application using Dash that visualizes the quantities of different fruits, such as apples, oranges, bananas, grapes, and strawberries. 
    Users will be able to select a specific fruit from a dropdown menu, and the app will display a bar chart showing the amount of that fruit.
    You can use the following data:
    data = {
        'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
        'Amount': [4, 1, 2, 5, 3],
    }

Expected Output
    Here is what the app looks like. 
    In the screenshot below, “Apples”
    When the user selects another fruit (e.g., Grapes), the graph updates by representing the amount of the chosen fruit:
    Here is a program structure to get you started. 
    
    import dash
    from dash import dcc, html
    from dash.dependencies import Input, Output
    import pandas as pd
    import plotly.express as px

    # Sample data
    data = {
        'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
        'Amount': [4, 1, 2, 5, 3],
    }

    df = pd.DataFrame(data)
    # Initialize the Dash app
    app = ...

    # Define the layout
    app.layout = html.Div([
    ...
    ...
    ])

    # Define the callback to update the graph
    @app.callback(
    ...
    ...
    )
    def update_graph(selected_fruit):
        ...
        ...

    # Run the app
    if __name__ == '__main__':
        app.run_server(debug=True)

Prerequisites
    Required Libraries: dash, plotly, pandas
                        pip install dash plotly pandas
'''

data = {
        'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
        'Amount': [4, 1, 2, 5, 3],
    }