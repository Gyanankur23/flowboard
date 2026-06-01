# Installation & Quick Start Guide

## System Requirements

- **Python**: 3.8+
- **RAM**: Minimum 1GB (recommended 4GB+)
- **OS**: Linux, macOS, Windows

## Installation

### Option 1: PyPI (Recommended)

```bash
pip install flowboard
```

This installs the latest stable version from PyPI.

### Option 2: Development (from Source)

```bash
git clone https://github.com/gyanankur23/flowboard.git
cd flowboard
pip install -e .[dev]
```

This installs the development version with test dependencies.

### Verify Installation

```bash
python -c "import flowboard; print(flowboard.__version__)"
# Output: 0.1.1
```

---

## 5-Minute Quick Start

### Step 1: Create Sample Data

```python
import tempfile
import os
from pathlib import Path

# Create sample CSV
csv_data = """date,region,category,amount,cost
2024-01-01,North America,Electronics,1200,600
2024-01-01,Europe,Clothing,350,140
2024-01-02,Asia,Electronics,1500,700
2024-01-02,North America,Home,450,180
"""

# Write to file
with open('sales.csv', 'w') as f:
    f.write(csv_data)
```

### Step 2: Load & Model Data

```python
import flowboard as fb

# Load data
table = fb.load_csv('sales.csv')
print(f"Loaded table: {table}")

# Define semantic model
model = fb.SemanticModel()
model.add_table(
    table,
    dimensions=['date', 'region', 'category'],
    measures={
        'revenue': 'SUM(amount)',
        'profit': 'SUM(amount - cost)',
        'avg_price': 'AVG(amount)',
        'order_count': 'COUNT(*)'
    }
)
```

### Step 3: Query with Intent

```python
# Natural business questions
result = fb.query("revenue by region", model)
print(result)
# Output: [{'region': 'Asia', 'revenue': 1500}, {'region': 'Europe', 'revenue': 350}, ...]

result = fb.query("profit by category", model)
print(result)
# Output: [{'category': 'Clothing', 'profit': 210}, {'category': 'Electronics', 'profit': 1400}, ...]
```

### Step 4: Visualize

```python
# Create interactive chart
result = fb.query("revenue by region", model)
chart = fb.chart(result)

# Display in Jupyter notebook
chart.show()

# Or save to HTML file
chart.write_html('revenue_by_region.html')
```

---

## Full Example: E-Commerce Dashboard

```python
import flowboard as fb

# 1. Load your data
orders_table = fb.load_csv('orders.csv')
products_table = fb.load_csv('products.csv')

# 2. Create semantic model
model = fb.SemanticModel()

# Define orders metrics
model.add_table(
    'orders',
    dimensions=['date', 'customer_segment', 'region', 'product_category'],
    measures={
        'gmv': 'SUM(order_value)',
        'aov': 'AVG(order_value)',
        'orders': 'COUNT(DISTINCT order_id)',
        'units': 'SUM(quantity)',
        'customers': 'COUNT(DISTINCT customer_id)'
    }
)

# 3. Define relationships
model.add_relationship('orders', 'product_id', 'products', 'id')

# 4. Run analytics
metrics = {
    'revenue_by_region': fb.query("gmv by region", model),
    'orders_by_segment': fb.query("orders by customer_segment", model),
    'units_by_category': fb.query("units by product_category", model)
}

# 5. Visualize
for name, result in metrics.items():
    chart = fb.chart(result)
    chart.write_html(f'{name}.html')
    print(f"✓ Generated {name}.html")
```

---

## Data Loading

### CSV Files

```python
import flowboard as fb

# Auto-detect schema from CSV
table = fb.load_csv('data.csv')
print(table)  # Returns: 'data'
```

**Features**:
- Automatic type detection
- Handles headers, missing values, quotes
- Efficient parsing with DuckDB

### Parquet Files

```python
# Load columnar format
table = fb.load_parquet('data.parquet')
```

**Benefits**:
- Column-oriented storage
- Better compression
- Faster for analytics

### Excel Files

```python
# Load from XLSX
table = fb.load_xlsx('budget.xlsx')
```

**Notes**:
- Loads first sheet by default
- Uses pandas for parsing

### Loading Multiple Files

```python
# Create a multi-table model
model = fb.SemanticModel()

sales = fb.load_csv('sales.csv')
model.add_table(sales, 
    dimensions=['month', 'region'],
    measures={'revenue': 'SUM(amount)'}
)

customers = fb.load_csv('customers.csv')
model.add_table(customers,
    dimensions=['segment'],
    measures={'count': 'COUNT(*)'}
)

# Define relationships
model.add_relationship('sales', 'customer_id', 'customers', 'id')
```

---

## Query Syntax

### Basic Intent Format

```
"<measure> by <dimension>"
```

**Examples**:
```python
fb.query("revenue by month", model)
fb.query("profit by region", model)
fb.query("count by category", model)
```

### Available Query Patterns

```python
# Single dimension
result = fb.query("revenue by region", model)

# Time-based
result = fb.query("units by date", model)

# Multi-segment
result = fb.query("profit by product_category", model)

# Custom measures
result = fb.query("avg_price by region", model)
```

### Error Handling

```python
try:
    result = fb.query("invalid_metric by region", model)
except ValueError as e:
    print(f"Query Error: {e}")
    # Output: Query Error: No table found with metric 'invalid_metric' and dimension 'region'
    #         Available measures: revenue, profit
    #         Available dimensions: region, category
```

---

## Visualization

### Interactive Bar Charts

```python
result = fb.query("revenue by region", model)
chart = fb.chart(result)

# Display options
chart.show()  # Jupyter/interactive environments
chart.write_html('chart.html')  # Save to file
```

### Customization

```python
result = fb.query("revenue by region", model)
fig = fb.chart(result)

# Modify Plotly figure
fig.update_layout(
    title="Revenue by Region",
    xaxis_title="Region",
    yaxis_title="Revenue ($)",
    height=600,
    template='plotly_dark'
)

fig.show()
```

### Export Formats

```python
fig = fb.chart(result)

# HTML
fig.write_html('chart.html')

# PNG (requires kaleido)
fig.write_image('chart.png')

# PDF
fig.write_image('chart.pdf')

# Static SVG
fig.write_image('chart.svg')
```

---

## Working with Results

### As List of Dictionaries

```python
result = fb.query("revenue by region", model)

# Iterate through results
for row in result:
    print(f"{row['region']}: ${row['revenue']:,.2f}")

# Access specific row
first = result[0]
region = first['region']
revenue = first['revenue']
```

### Convert to DataFrame

```python
import pandas as pd

result = fb.query("revenue by region", model)
df = pd.DataFrame(result)

# Now use pandas for further analysis
print(df.describe())
df.to_csv('results.csv', index=False)
```

### Aggregate Results

```python
result = fb.query("revenue by region", model)

total_revenue = sum(row['revenue'] for row in result)
avg_revenue = total_revenue / len(result)
max_region = max(result, key=lambda x: x['revenue'])

print(f"Total: ${total_revenue:,.2f}")
print(f"Average: ${avg_revenue:,.2f}")
print(f"Top Region: {max_region['region']}")
```

---

## Troubleshooting

### ImportError: No module named 'flowboard'

```bash
# Solution: Install the package
pip install flowboard

# Or verify Python path
python -c "import sys; print(sys.path)"
```

### FileNotFoundError: CSV file not found

```python
# Problem
table = fb.load_csv('data.csv')  # File doesn't exist

# Solution
import os
if os.path.exists('data.csv'):
    table = fb.load_csv('data.csv')
else:
    print("File not found!")
```

### ValueError: Invalid query format

```python
# Problem
result = fb.query("revenue", model)  # Missing "by dimension"

# Solution
result = fb.query("revenue by region", model)  # Correct format
```

### ValueError: No table found

```python
# Problem
result = fb.query("invalid_metric by region", model)

# Solution: Check available metrics
print(model.tables)
```

---

## Performance Tips

### 1. Use Parquet for Large Files
```python
# Better for 1GB+ files
table = fb.load_parquet('large_data.parquet')  # Faster than CSV
```

### 2. Pre-Aggregate Data
```python
# Instead of loading raw data
# Pre-aggregate to monthly summary
table = fb.load_csv('monthly_summary.csv')
```

### 3. Filter Before Loading
```python
# If using DuckDB directly
con.execute("""
    CREATE TABLE recent_data AS
    SELECT * FROM read_csv_auto('data.csv')
    WHERE date >= '2024-01-01'
""")
```

### 4. Index Frequently Queried Dimensions
```python
from flowboard.engine import con

# DuckDB auto-indexes large tables
# No explicit action needed
```

---

## Next Steps

1. **Run the demo**: `python demo.py`
2. **Read the docs**: Check [README.md](README.md)
3. **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md)
4. **Get help**: Open an issue on GitHub

---

**Happy analytics! 🚀**
