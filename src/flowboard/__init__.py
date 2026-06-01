"""
Flowboard: Power BI-style analytics with DuckDB.

A lightweight, in-memory analytics framework for building production-grade
semantic models and intent-driven queries over multi-table datasets.

Quick Start:
    >>> import flowboard as fb
    >>> table = fb.load_csv('data.csv')
    >>> model = fb.SemanticModel()
    >>> model.add_table('data', dimensions=['category'], measures={'revenue': 'SUM(amount)'})
    >>> result = fb.query("revenue by category", model)
    >>> chart = fb.chart(result)
    >>> chart.show()
"""

from .io import load_csv, load_parquet, load_xlsx
from .model import SemanticModel
from .query import query
from .viz import chart

__version__ = "0.1.1"
__author__ = "Gyanankur Baruah"
__license__ = "MIT"

__all__ = [
    'load_csv',
    'load_parquet', 
    'load_xlsx',
    'SemanticModel',
    'query',
    'chart',
]