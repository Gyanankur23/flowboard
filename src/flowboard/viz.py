"""
Visualization module for Flowboard.

Generates interactive charts from query results using Plotly.
"""

from typing import List, Dict, Any
import plotly.express as px
import plotly.graph_objects as go


def chart(result: List[Dict[str, Any]]) -> go.Figure:
    """
    Generate an interactive bar chart from query results.
    
    Creates a Plotly bar chart with the first column as X-axis
    and the second column as Y-axis values.
    
    Args:
        result: List of dictionaries from a query operation
                Must have exactly 2 columns
        
    Returns:
        Plotly Figure object (use .show() to display or .write_html() to save)
        
    Raises:
        ValueError: If result is empty or has != 2 columns
        
    Example:
        >>> result = fb.query('revenue by region', model)
        >>> fig = fb.chart(result)
        >>> fig.show()  # Display interactively
        >>> fig.write_html('chart.html')  # Save to file
    """
    if not result:
        raise ValueError("No data to chart: result is empty")
    
    keys = list(result[0].keys())
    if len(keys) != 2:
        raise ValueError(
            f"Query result must have exactly 2 columns for charting, got {len(keys)}\n"
            f"Columns: {keys}"
        )
    
    x_col, y_col = keys
    
    # Create interactive Plotly bar chart
    fig = px.bar(
        result,
        x=x_col,
        y=y_col,
        title=f"{y_col.title()} by {x_col.title()}",
        labels={
            x_col: x_col.replace('_', ' ').title(),
            y_col: y_col.replace('_', ' ').title()
        },
        hover_data=result
    )
    
    # Enhance layout for better presentation
    fig.update_layout(
        hovermode='x unified',
        template='plotly_white',
        height=500,
        xaxis_title=x_col.replace('_', ' ').title(),
        yaxis_title=y_col.replace('_', ' ').title(),
    )
    
    return fig
