'''
# Task 1:
# read the data and display the:
    - sum of cars sold in each month
    - Total yearly sales by each manufacture
'''
companies = []
sales = []

with open("./carSale.csv", "r") as file:
    lines = file.readlines
    car_n_sales = [row for row in lines]
    companies = [line for line in file]
    pass
