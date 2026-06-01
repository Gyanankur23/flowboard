"""
DuckDB execution engine for Flowboard.

Provides the in-memory SQL execution layer with sub-millisecond query performance.
All data is loaded into a persistent in-memory DuckDB connection.
"""

import duckdb

# Global in-memory DuckDB connection
con = duckdb.connect(':memory:')


def execute(sql: str) -> list:
    """
    Execute SQL query against the in-memory DuckDB database.
    
    Args:
        sql: SQL query string
        
    Returns:
        List of result tuples
        
    Example:
        >>> result = execute('SELECT * FROM sales WHERE region = \"North America\"')
    """
    return con.execute(sql).fetchall()
