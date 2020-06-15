# dashboard_generator.py

import os
import csv
import plotly.graph_objects as go

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

#TOP SELLING PRODUCTS

product_dict = {}
with open(file_path, "r") as csv_file:  
    reader = csv.DictReader(csv_file)  
    for r in reader:
        product_name = r["product"]
        product_sales = float(r["sales price"])
        if r["product"] not in product_dict:
            product_dict[product_name] = product_sales
        else:
            product_dict[product_name] += product_sales

# >Reverse Sort by  Sublist https://stackoverflow.com/questions/18142090/python-sort-a-list-of-lists-by-an-item-in-the-sublist
desc_new_list = sorted(product_dict.items(), key=lambda x: x[1], reverse=True)

print("TOP SELLING PRODUCTS:")
for i in range(3):
    print(
        str(i + 1)
        + ") "
        + desc_new_list[i][0]
        + " : "
        + str(to_usd(desc_new_list[i][1]))
    )

