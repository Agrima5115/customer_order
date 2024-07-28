import csv
from collections import defaultdict
from datetime import datetime

def process_orders(csv_file):
    total_revenue_by_month = defaultdict(float)
    total_revenue_by_product = defaultdict(float)
    total_revenue_by_customer = defaultdict(float)

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            order_date = datetime.strptime(row['order_date'], '%Y-%m-%d')
            month = order_date.strftime('%Y-%m')
            product_revenue = float(row['product_price']) * int(row['quantity'])
            
            total_revenue_by_month[month] += product_revenue
            total_revenue_by_product[row['product_name']] += product_revenue
            total_revenue_by_customer[row['customer_id']] += product_revenue
    
    return total_revenue_by_month, total_revenue_by_product, total_revenue_by_customer

def top_10_customers(total_revenue_by_customer):
    sorted_customers = sorted(total_revenue_by_customer.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_customers[:10]
    return top_10

def main():
    csv_file = 'D:/customer/app/orders.csv'
    total_revenue_by_month, total_revenue_by_product, total_revenue_by_customer = process_orders(csv_file)
    
    print("Total revenue by month:")
    for month, revenue in total_revenue_by_month.items():
        print(f"{month}: ${revenue:.2f}")
    
    print("\nTotal revenue by product:")
    for product, revenue in total_revenue_by_product.items():
        print(f"{product}: ${revenue:.2f}")
    
    print("\nTotal revenue by customer:")
    for customer_id, revenue in total_revenue_by_customer.items():
        print(f"Customer ID {customer_id}: ${revenue:.2f}")
    
    print("\nTop 10 customers by revenue:")
    top_customers = top_10_customers(total_revenue_by_customer)
    for rank, (customer_id, revenue) in enumerate(top_customers, start=1):
        print(f"{rank}. Customer ID {customer_id}: ${revenue:.2f}")

if __name__ == "__main__":
    main()
