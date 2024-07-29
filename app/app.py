import csv
from collections import defaultdict
from datetime import datetime

def process_orders(csv_file):
    # Initialize defaultdicts to store total revenue by month, product, and customer
    total_revenue_by_month = defaultdict(float)
    total_revenue_by_product = defaultdict(float)
    total_revenue_by_customer = defaultdict(float)

    # Open the CSV file and read its contents
    with open(csv_file, 'r') as file:
        # Use csv.DictReader to read the CSV file as a dictionary
        reader = csv.DictReader(file)
        for row in reader:
            # Convert order_date string to datetime object
            order_date = datetime.strptime(row['order_date'], '%Y-%m-%d')
            # Extract month from order_date and format it as 'YYYY-MM'
            month = order_date.strftime('%Y-%m')
            # Calculate product revenue by multiplying product_price by quantity
            product_revenue = float(row['product_price']) * int(row['quantity'])
            
            # Update total revenue by month, product, and customer
            total_revenue_by_month[month] += product_revenue
            total_revenue_by_product[row['product_name']] += product_revenue
            total_revenue_by_customer[int(row['customer_id'])] += product_revenue
    
    # Convert defaultdicts to sorted lists of tuples
    total_revenue_by_month = sorted(total_revenue_by_month.items())
    total_revenue_by_product = sorted(total_revenue_by_product.items())
    total_revenue_by_customer = sorted(total_revenue_by_customer.items(), key=lambda x: -x[1])
    
    # Return the accumulated revenues by month, product, and customer
    return total_revenue_by_month, total_revenue_by_product, total_revenue_by_customer

def top_10_customers(total_revenue_by_customer):
    # Select the top 10 customers based on revenue
    top_10 = total_revenue_by_customer[:10]
    return top_10

def main():
    csv_file = 'D:/customer/app/orders.csv'
    # Process orders to get total revenues by month, product, and customer
    total_revenue_by_month, total_revenue_by_product, total_revenue_by_customer = process_orders(csv_file)
    
    # Print total revenue by month
    print("Total revenue by month:")
    for month, revenue in total_revenue_by_month:
        print(f"{month}: ${revenue:.2f}")
    
    # Print total revenue by product
    print("\nTotal revenue by product:")
    for product, revenue in total_revenue_by_product:
        print(f"{product}: ${revenue:.2f}")
    
    # Print total revenue by customer
    print("\nTotal revenue by customer:")
    for customer_id, revenue in total_revenue_by_customer:
        print(f"Customer ID {customer_id}: ${revenue:.2f}")
    
    # Print top 10 customers by revenue
    print("\nTop 10 customers by revenue:")
    top_customers = top_10_customers(total_revenue_by_customer)
    for rank, (customer_id, revenue) in enumerate(top_customers, start=1):
        print(f"{rank}. Customer ID {customer_id}: ${revenue:.2f}")

if __name__ == "__main__":
    main()
