import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

# Defining the options for each categorical column
branches = ['A', 'B', 'C']
cities = ['Sydney', 'Brisbane', 'Perth', 'Darwin', 'Tasmania']
customer_types = ['Member', 'Normal']
genders = ['Male', 'Female']
product_lines = ['Health and beauty', 'Electronic accessories', 'Home and lifestyle', 
                 'Sports and travel', 'Food and beverages', 'Fashion accessories']
payment_methods = ['Cash', 'Credit card', 'Ewallet']

# Generating 10 rows of synthetic data
rows = []
for i in range(10):
    invoice_id = fake.unique.bothify(text='INV#####')
    branch = random.choice(branches)
    city = random.choice(cities)
    customer_type = random.choice(customer_types)
    gender = random.choice(genders)
    product_line = random.choice(product_lines)
    unit_price = round(random.uniform(5, 100), 2)
    quantity = random.randint(1, 10)
    tax_5 = round((unit_price * quantity) * 0.05, 2)
    total = round((unit_price * quantity) + tax_5, 2)
    date = fake.date_between(start_date='-1y', end_date='today').strftime('%m/%d/%Y')
    time = fake.time()
    payment = random.choice(payment_methods)
    cogs = round(unit_price * quantity, 2)
    gross_margin_percentage = 4.76  # Assuming constant as in typical examples
    gross_income = tax_5
    rating = round(random.uniform(4, 10), 1)

    row = [invoice_id, branch, city, customer_type, gender, product_line,
           unit_price, quantity, tax_5, total, date, time, payment, 
           cogs, gross_margin_percentage, gross_income, rating]
    
    rows.append(row)

# Creating the DataFrame
columns = ['Invoice id', 'Branch', 'City', 'Customer type', 'Gender', 'Product line', 
           'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date', 'Time', 'Payment', 
           'cogs', 'gross margin percentage', 'gross income', 'Rating']

df = pd.DataFrame(rows, columns=columns)

# Export to CSV
df.to_csv('add_data.csv', index=False)

print("CSV file 'add_data.csv' has been generated successfully.")
