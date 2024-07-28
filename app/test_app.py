import unittest
import os
import pandas as pd
from app import process_orders

class TestApp(unittest.TestCase):
    def setUp(self):
        # Sample CSV data for testing
        self.csv_data = """order_id,customer_id,order_date,product_id,product_name,product_price,quantity
1,101,2023-11-15,1,Smartphone,799.99,2
2,123,2024-03-08,2,Laptop,1299.99,1
3,156,2023-07-22,3,Headphones,199.99,3
4,187,2024-02-14,4,Tablet,399.99,2
5,101,2023-12-25,5,Smartwatch,249.99,1
"""
        # Path to the temporary CSV file
        self.csv_file = 'test_orders.csv'
        # Write the sample CSV data to the file
        with open(self.csv_file, 'w') as f:
            f.write(self.csv_data)
    
    def tearDown(self):
        # Remove the temporary CSV file after the test is completed
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
    
    def test_process_orders(self):
        # Define the expected results for monthly, product, and customer revenues
        expected_monthly_revenue = pd.Series({
            pd.Timestamp('2023-07-31'): 599.97,
            pd.Timestamp('2023-11-30'): 1599.98,
            pd.Timestamp('2023-12-31'): 249.99,
            pd.Timestamp('2024-02-29'): 799.98,
            pd.Timestamp('2024-03-31'): 1299.99,
        }).sort_index()
        
        expected_product_revenue = pd.Series({
            'Headphones': 599.97,
            'Laptop': 1299.99,
            'Smartphone': 1599.98,
            'Smartwatch': 249.99,
            'Tablet': 799.98,
        }).sort_index()
        
        expected_customer_revenue = pd.Series({
            101: 1849.97,
            123: 1299.99,
            156: 599.97,
            187: 799.98,
        }).sort_index()

        expected_top_10_customers = expected_customer_revenue.sort_values(ascending=False).head(10)
        
        # Call the process_orders function and get the results
        monthly_revenue, product_revenue, customer_revenue = process_orders(self.csv_file)
        top_10_customers = customer_revenue.sort_values(ascending=False).head(10)
        
        # Assert that the calculated results match the expected results
        pd.testing.assert_series_equal(monthly_revenue.sort_index(), expected_monthly_revenue)
        pd.testing.assert_series_equal(product_revenue.sort_index(), expected_product_revenue)
        pd.testing.assert_series_equal(customer_revenue.sort_index(), expected_customer_revenue)
        pd.testing.assert_series_equal(top_10_customers.sort_index(), expected_top_10_customers)

if __name__ == "__main__":
    unittest.main()
