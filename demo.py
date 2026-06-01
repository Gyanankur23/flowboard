#!/usr/bin/env python3
"""
Flowboard Demo: Real-World E-Commerce Analytics

This script demonstrates Flowboard's capabilities using a realistic
SaaS/E-Commerce analytics scenario. It showcases:

1. Multi-format data loading (CSV)
2. Semantic model definition with dimensions and measures
3. Intent-driven queries
4. Interactive visualization
5. Business KPI calculation

Run: python demo.py
"""

import tempfile
import os
import flowboard as fb


def create_sample_data():
    """Create realistic e-commerce dataset."""
    data = """date,region,product_category,customer_segment,order_id,amount,cost,units
2024-01-01,North America,Electronics,Premium,ORD001,1200,600,2
2024-01-01,North America,Clothing,Standard,ORD002,350,140,5
2024-01-01,Europe,Electronics,Premium,ORD003,1500,700,3
2024-01-02,Asia,Clothing,Budget,ORD004,180,80,4
2024-01-02,North America,Home,Standard,ORD005,450,180,3
2024-01-02,Europe,Electronics,Standard,ORD006,800,320,1
2024-01-03,Asia,Electronics,Premium,ORD007,2000,900,4
2024-01-03,North America,Home,Budget,ORD008,250,100,2
2024-01-04,Europe,Clothing,Premium,ORD009,600,240,2
2024-01-04,Asia,Electronics,Budget,ORD010,400,200,1
2024-01-05,North America,Electronics,Standard,ORD011,950,400,2
2024-01-05,Europe,Home,Standard,ORD012,520,250,4
2024-01-05,Asia,Clothing,Premium,ORD013,850,300,3
2024-01-06,North America,Clothing,Premium,ORD014,700,280,2
2024-01-06,Europe,Electronics,Budget,ORD015,600,300,1
"""
    return data


def main():
    print("=" * 70)
    print("FLOWBOARD DEMO: E-Commerce Analytics Pipeline")
    print("=" * 70)
    print()

    # Step 1: Create temporary data file
    print("📊 Step 1: Loading Data")
    print("-" * 70)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        csv_path = os.path.join(tmpdir, 'ecommerce_orders.csv')
        with open(csv_path, 'w') as f:
            f.write(create_sample_data())
        
        # Load data into Flowboard
        table = fb.load_csv(csv_path)
        print(f"✓ Loaded table: '{table}' with 15 sample orders")
        print()

        # Step 2: Define Semantic Model
        print("🎯 Step 2: Defining Semantic Model")
        print("-" * 70)
        
        model = fb.SemanticModel()
        
        # Define dimensions (categorical grouping attributes)
        dimensions = ['date', 'region', 'product_category', 'customer_segment']
        
        # Define measures (aggregated metrics)
        measures = {
            'revenue': 'SUM(amount)',
            'cost': 'SUM(cost)',
            'profit': 'SUM(amount - cost)',
            'units_sold': 'COUNT(units)',
            'avg_order_value': 'AVG(amount)',
            'orders': 'COUNT(DISTINCT order_id)'
        }
        
        model.add_table(table, dimensions=dimensions, measures=measures)
        
        print(f"✓ Registered table with {len(dimensions)} dimensions")
        print(f"  Dimensions: {', '.join(dimensions)}")
        print(f"✓ Registered {len(measures)} business metrics")
        for metric, formula in measures.items():
            print(f"  - {metric:20s} → {formula}")
        print()

        # Step 3: Execute Semantic Queries
        print("📈 Step 3: Semantic Query Examples")
        print("-" * 70)
        print()
        
        # Query 1: Revenue by Region
        print("Query 1️⃣  : 'revenue by region'")
        print("Business Question: Which region generates the most revenue?")
        try:
            result = fb.query("revenue by region", model)
            print("Results:")
            for row in result:
                region = row['region']
                revenue = row['revenue']
                print(f"  {region:20s}: ${revenue:,.2f}")
            print()
        except Exception as e:
            print(f"  Error: {e}")
            print()

        # Query 2: Profit by Product Category
        print("Query 2️⃣  : 'profit by product_category'")
        print("Business Question: Which product categories are most profitable?")
        try:
            result = fb.query("profit by product_category", model)
            print("Results:")
            for row in result:
                category = row['product_category']
                profit = row['profit']
                print(f"  {category:20s}: ${profit:,.2f}")
            print()
        except Exception as e:
            print(f"  Error: {e}")
            print()

        # Query 3: Orders by Customer Segment
        print("Query 3️⃣  : 'orders by customer_segment'")
        print("Business Question: Which customer segment has the most orders?")
        try:
            result = fb.query("orders by customer_segment", model)
            print("Results:")
            for row in result:
                segment = row['customer_segment']
                orders = row['orders']
                print(f"  {segment:20s}: {orders} orders")
            print()
        except Exception as e:
            print(f"  Error: {e}")
            print()

        # Query 4: Units Sold by Date
        print("Query 4️⃣  : 'units_sold by date'")
        print("Business Question: What's the daily sales volume?")
        try:
            result = fb.query("units_sold by date", model)
            print("Results:")
            for row in result:
                date = row['date']
                units = row['units_sold']
                print(f"  {date}: {units} units")
            print()
        except Exception as e:
            print(f"  Error: {e}")
            print()

        # Step 4: Visualization
        print("🎨 Step 4: Visualization & Export")
        print("-" * 70)
        print()
        
        # Generate a chart
        result = fb.query("revenue by region", model)
        chart = fb.chart(result)
        
        print("✓ Generated interactive chart: 'Revenue by Region'")
        print("  Chart type: Interactive Bar Chart (Plotly)")
        print("  To display in Jupyter/app: chart.show()")
        print("  To save as HTML: chart.write_html('chart.html')")
        print()

        # Step 5: Business Insights
        print("💡 Step 5: Derived Business Insights")
        print("-" * 70)
        print()
        
        # Calculate KPIs
        total_revenue = fb.query("revenue by region", model)
        total_revenue_sum = sum(row['revenue'] for row in total_revenue)
        
        total_profit = fb.query("profit by product_category", model)
        total_profit_sum = sum(row['profit'] for row in total_profit)
        
        profit_margin = (total_profit_sum / total_revenue_sum * 100) if total_revenue_sum > 0 else 0
        
        print(f"Total Revenue:   ${total_revenue_sum:,.2f}")
        print(f"Total Profit:    ${total_profit_sum:,.2f}")
        print(f"Profit Margin:   {profit_margin:.1f}%")
        print()

    print("=" * 70)
    print("✅ Demo Complete!")
    print("=" * 70)
    print()
    print("Next Steps:")
    print("1. Try with your own CSV data: fb.load_csv('your_file.csv')")
    print("2. Define custom dimensions and measures in SemanticModel")
    print("3. Use fb.query() for different business questions")
    print("4. Export charts: chart.write_html('output.html')")
    print()
    print(f"Flowboard v{fb.__version__}")
    print("Built for data teams | https://github.com/gyanankur23/flowboard")
    print()


if __name__ == "__main__":
    main()
