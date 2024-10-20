# Calculate the Total Sales

# You are given two dictionaries:

# A dictionary called items_info that contains information about the items and their prices.
# A dictionary called sales_info that contains information about the quantities sold for each item.
# Write a Python program that calculates the total revenue.

# Total revenue: 26.5
# Instructions: Items_Info contains the price of said item as the value. Sales_Info contains the quantity of said item as the value.

# Calculate the revenue using the following formula:

# revenue = quantity * price

# Also create a comprehensive test suite (that contains at least a success case, failure case, and edge case).

def total_sales():
    items_info = {"apple": 0.5, "banana": 0.3, "orange": 0.7,"grape": 1.2}
    sales_info = {"apple": 10, "banana": 5, "orange": 8, "grape": 12}
    total = 0
    for key in items_info:
        revenue = items_info[key] * sales_info[key]
        # print(value)
        total = total + revenue
    return total


