# List of Items in Menu
menu = ["Coffee", "Milk", "Croissant", "Sanwich", "Toast"]

# Dictionary of the stock of each item in the menu
stock = {
    "Coffee": 23,
    "Milk": 59,
    "Croissant": 5,
    "Sanwich": 3,
    "Toast": 45
}

# Dictionary of the price of each item in the menu
price = {
    "Coffee": 7.50,
    "Milk": 4.00,
    "Croissant": 7.00,
    "Sanwich": 4.00,
    "Toast": 2.50
}

total_stock = 0

# For loop goes through each item in the list and looks up the stock and the price of each item to find the total stock value.
for i in menu:
    total_stock +=  stock[i] * price[i]

print("Total worth of stock is: "+str(total_stock))