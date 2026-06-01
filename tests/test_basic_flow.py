import tempfile
import os
import flowboard as fb

def test_basic_flow():
    data = """month,region,amount,cost
Jan,East,100,50
Feb,East,200,100
Jan,West,150,75
Feb,West,250,125
"""
    
    with tempfile.TemporaryDirectory() as tmpdir:
        csv_path = os.path.join(tmpdir, 'sales.csv')
        with open(csv_path, 'w') as f:
            f.write(data)
        
        table = fb.load_csv(csv_path)
        assert table == 'sales'
        
        model = fb.SemanticModel()
        model.add_table('sales', dimensions=['month', 'region'], measures={'revenue': 'SUM(amount)', 'profit': 'SUM(amount - cost)'})
        
        result = fb.query("revenue by month", model)
        assert len(result) == 2
        assert 'month' in result[0]
        assert 'revenue' in result[0]
        
        chart = fb.chart(result)
        assert chart is not None