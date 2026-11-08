# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

import csv
from collections import defaultdict

try:
    with open("sales.csv") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print("No sales data found.")
    else:
        for row in rows:
            row["Sales_Amount"] = int(row["Sales_Amount"])
            row["Units_Sold"] = int(row["Units_Sold"])

        largest_sale = max(rows, key=lambda row: row["Sales_Amount"])
        average_sale = sum(row["Sales_Amount"] for row in rows) / len(rows)

        units_by_product = defaultdict(int)
        sales_by_product = defaultdict(int)

        for row in rows:
            product = row["Product"]
            units_by_product[product] += row["Units_Sold"]
            sales_by_product[product] += row["Sales_Amount"]

        top_product = max(units_by_product, key=units_by_product.get)

        print(f"Largest sale: ${largest_sale['Sales_Amount']:,} on {largest_sale['Date']}")
        print(f"Average sale amount: ${average_sale:,.2f}")
        print(
            f"Most units sold: {top_product} "
            f"({units_by_product[top_product]} units)"
        )

        print("\nTotal sales by product:")
        for product, total in sales_by_product.items():
            print(f"{product}: ${total:,}")
except FileNotFoundError:
    print("Error: sales.csv was not found.")
except (OSError, KeyError, ValueError) as error:
    print(f"Error reading or processing the sales data: {error}")


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget

# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows