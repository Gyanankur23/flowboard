"""
Intent-driven query engine for Flowboard.

Translates natural business intent ("metric by dimension") into
optimized SQL executed by DuckDB.
"""

from typing import List, Dict, Any
from .engine import execute
from .model import SemanticModel


def query(intent: str, model: SemanticModel) -> List[Dict[str, Any]]:
    """
    Execute an intent-driven query against a semantic model.
    
    Translates natural business questions like \"revenue by region\" into
    optimized SQL GROUP BY queries.
    
    Args:
        intent: Query intent in format \"<measure> by <dimension>\"
                E.g., \"revenue by region\", \"units by product_category\"
        model: Configured SemanticModel instance
        
    Returns:
        List of result rows as dictionaries
        
    Raises:
        ValueError: If intent format is invalid or metric/dimension not found
        
    Example:
        >>> model = SemanticModel()
        >>> model.add_table('sales',
        ...     dimensions=['region', 'month'],
        ...     measures={'revenue': 'SUM(amount)'}
        ... )
        >>> result = query('revenue by region', model)
        >>> for row in result:
        ...     print(f\"{row['region']}: ${row['revenue']:.2f}\")
    """
    # Parse intent into metric and dimension
    parts = intent.lower().split(' by ')
    
    if len(parts) != 2:
        raise ValueError(
            f"Invalid query format: '{intent}'\n"
            f"Expected format: '<measure> by <dimension>'\n"
            f"Example: 'revenue by region'"
        )
    
    metric = parts[0].strip()
    dimension = parts[1].strip()
    
    # Find table containing both metric (measure) and dimension
    table = None
    for table_name, table_info in model.tables.items():
        if (metric in table_info['measures'] and 
            dimension in table_info['dimensions']):
            table = table_name
            break
    
    if not table:
        available_measures = set()
        available_dimensions = set()
        for table_info in model.tables.values():
            available_measures.update(table_info['measures'].keys())
            available_dimensions.update(table_info['dimensions'])
        
        raise ValueError(
            f"No table found with metric '{metric}' and dimension '{dimension}'\n"
            f"Available measures: {', '.join(available_measures)}\n"
            f"Available dimensions: {', '.join(available_dimensions)}"
        )
    
    # Build and execute SQL query
    measure_expr = model.tables[table]['measures'][metric]
    sql = (
        f"SELECT {dimension}, {measure_expr} AS {metric} "
        f"FROM {table} "
        f"GROUP BY {dimension} "
        f"ORDER BY {dimension}"
    )
    
    # Execute and format results
    result = execute(sql)
    columns = [dimension, metric]
    return [dict(zip(columns, row)) for row in result]
