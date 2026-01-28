from .engine import execute

def query(intent, model):
    parts = intent.lower().split(' by ')
    if len(parts) != 2:
        raise ValueError("Intent must be 'metric by dimension'")
    
    metric, dimension = parts
    metric = metric.strip()
    dimension = dimension.strip()
    
    # Find table with the metric and dimension
    table = None
    for t, info in model.tables.items():
        if metric in info['measures'] and dimension in info['dimensions']:
            table = t
            break
    
    if not table:
        raise ValueError(f"No table found for metric '{metric}' and dimension '{dimension}'")
    
    measure_expr = model.tables[table]['measures'][metric]
    sql = f"SELECT {dimension}, {measure_expr} AS {metric} FROM {table} GROUP BY {dimension} ORDER BY {dimension}"
    

    result = execute(sql)
    columns = [dimension, metric]
    return [dict(zip(columns, row)) for row in result]