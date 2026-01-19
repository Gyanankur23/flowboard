import plotly.express as px

def chart(result):
    if not result:
        raise ValueError("No data to chart")
    
    keys = list(result[0].keys())
    if len(keys) != 2:
        raise ValueError("Query result must have exactly 2 columns for charting")
    
    x_col, y_col = keys
    fig = px.bar(result, x=x_col, y=y_col)
    return fig