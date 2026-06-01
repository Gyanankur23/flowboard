"""
Semantic model definition for Flowboard.

Provides the SemanticModel class to define dimensions, measures, and
relationships across data tables.
"""

from typing import Dict, List, Tuple


class SemanticModel:
    """
    Define a semantic data model with dimensions and measures.
    
    A semantic model captures the business logic layer on top of raw data,
    enabling intent-driven queries and self-service analytics.
    
    Attributes:
        tables: Dict mapping table names to dimension/measure definitions
        relationships: List of foreign key relationships between tables
        
    Example:
        >>> model = SemanticModel()
        >>> model.add_table('sales', 
        ...     dimensions=['date', 'region'],
        ...     measures={'revenue': 'SUM(amount)', 'profit': 'SUM(amount-cost)'}
        ... )
        >>> model.add_relationship('sales', 'customer_id', 'customers', 'id')
    """
    
    def __init__(self):
        """Initialize an empty semantic model."""
        self.tables: Dict[str, Dict] = {}
        self.relationships: List[Tuple[str, str, str, str]] = []
    
    def add_table(self, table_name: str, dimensions: List[str], measures: Dict[str, str]) -> None:
        """
        Register a table in the semantic model.
        
        Args:
            table_name: Name of the table in the database
            dimensions: List of column names that serve as grouping dimensions
            measures: Dict mapping measure names to SQL aggregate expressions
                     E.g., {'revenue': 'SUM(amount)', 'profit': 'SUM(amount-cost)'}
                     
        Raises:
            ValueError: If dimensions or measures are empty
            
        Example:
            >>> model.add_table('sales',
            ...     dimensions=['month', 'region', 'product'],
            ...     measures={
            ...         'revenue': 'SUM(amount)',
            ...         'units': 'COUNT(*)',
            ...         'avg_price': 'AVG(price)'
            ...     }
            ... )
        """
        if not dimensions:
            raise ValueError("Must provide at least one dimension")
        if not measures:
            raise ValueError("Must provide at least one measure")
            
        self.tables[table_name] = {
            'dimensions': dimensions,
            'measures': measures
        }
    
    def add_relationship(self, table1: str, col1: str, table2: str, col2: str) -> None:
        """
        Define a foreign key relationship between two tables.
        
        Args:
            table1: Source table name
            col1: Foreign key column in source table
            table2: Target table name
            col2: Primary key column in target table
            
        Example:
            >>> model.add_relationship('orders', 'customer_id', 'customers', 'id')
            >>> model.add_relationship('orders', 'product_id', 'products', 'id')
        """
        self.relationships.append((table1, col1, table2, col2))
