# dashboard_generator.py

import os
import csv

#INPUT/DATA VALIDATION

x = input("Please input sales data to be analyzed (format: sales-YYYYMM.csv): ")
print(x)  

file_path = os.path.join(os.path.dirname(__file__), "data", x)

if (os.path.isfile(file_path)) == False:
    print("Cannot Find That Data File")
    exit()

#TOTAL MONTHLY SALES
print("-----------------------")
print("CRUNCHING THE DATA...")

with open(file_path, "r") as csv_file:  
    reader = csv.DictReader(csv_file)  
    monthly_sales = []
    for x in reader:
        monthly_sales.append(float(x["sales price"]))

def to_usd(my_price):
    return f"${my_price:,.2f}"

total_sales = to_usd(sum(monthly_sales))

print("-----------------------")
print("TOTAL MONTHLY SALES: " + total_sales)
print("-----------------------")

