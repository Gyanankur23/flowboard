# Flowboard

A Power BI-style analytics package using DuckDB for fast, in-memory data analysis.

[![Build & Publish to PyPI](https://github.com/Gyanankur23/flowboard/actions/workflows/publish.yml/badge.svg)](https://github.com/Gyanankur23/flowboard/actions/workflows/publish.yml)

## Installation

```bash
pip install flowboard
```

For development:
```bash
git clone <repo>
cd flowboard
pip install -e .[dev]
```

## Quick Start

```python
import flowboard as fb

# Load data (example)
data = fb.load_csv('sales.csv')

# Define semantic model
model = fb.SemanticModel()
model.add_table('sales', dimensions=['month', 'region'], measures={'revenue': 'SUM(amount)', 'profit': 'SUM(amount - cost)'})

# Query with intent
result = fb.query("revenue by month", model)

# Visualize
chart = fb.chart(result)
chart.show()
```

## Features

- Load large CSV, Parquet, XLSX files
- Multi-table relationships
- Semantic modeling with dimensions and measures
- Intent-first query DSL
- One-line chart generation with Plotly
