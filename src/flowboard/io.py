"""
Data loading module for Flowboard.

Provides functions to load data from various formats (CSV, Parquet, XLSX)
into the DuckDB in-memory execution engine.
"""

import os
import pandas as pd
from .engine import con


def load_csv(path: str) -> str:
    """
    Load a CSV file into DuckDB with automatic type detection.
    
    Args:
        path: File path to CSV file
        
    Returns:
        Table name (derived from filename without extension)
        
    Raises:
        FileNotFoundError: If CSV file doesn't exist
        
    Example:
        >>> table = fb.load_csv('sales.csv')
        >>> print(table)
        'sales'
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV file not found: {path}")
    
    table_name = os.path.splitext(os.path.basename(path))[0]
    con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{path}')")
    return table_name


def load_parquet(path: str) -> str:
    """
    Load a Parquet file into DuckDB.
    
    Args:
        path: File path to Parquet file
        
    Returns:
        Table name (derived from filename without extension)
        
    Raises:
        FileNotFoundError: If Parquet file doesn't exist
        
    Example:
        >>> table = fb.load_parquet('data.parquet')
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Parquet file not found: {path}")
    
    table_name = os.path.splitext(os.path.basename(path))[0]
    con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM read_parquet('{path}')")
    return table_name


def load_xlsx(path: str) -> str:
    """
    Load an Excel file into DuckDB.
    
    Args:
        path: File path to Excel (.xlsx) file
        
    Returns:
        Table name (derived from filename without extension)
        
    Raises:
        FileNotFoundError: If Excel file doesn't exist
        
    Example:
        >>> table = fb.load_xlsx('budget.xlsx')
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Excel file not found: {path}")
    
    table_name = os.path.splitext(os.path.basename(path))[0]
    df = pd.read_excel(path)
    con.register('temp_df', df)
    con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM temp_df")
    return table_name
