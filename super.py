# Define a dictionary of available goods and their prices
goods = {
    "apple": 1.00,
    "banana": 0.50,
    "orange": 0.75,
    "bread": 2.50,
    "milk": 1.75
}

# Initialize an empty list to store the customer's purchases
purchases = []

# Function to display the available goods and prices
def display_goods():
    print("Available goods:")
    for item, price in goods.items():
        print(f"{item}: ${price:.2f}")

# Function to process customer's purchases
def buy_goods():
    while True:
        display_goods()
        item = input("Enter the item you want to buy: ").lower()
        if item in goods:
            quantity = int(input(f"Enter the quantity of {item}s: "))
            purchases.append((item, quantity))
            more = input("Do you want to buy more? (yes/no): ").lower()
            if more != 'yes':
                break
        else:
            print("Sorry, that item is not available.")

# Function to print the customer's receipt
def print_receipt():
    total_cost = 0
    print("\nReceipt:")
    for item, quantity in purchases:
        price = goods[item]
        cost = price * quantity
        total_cost += cost
        print(f"{item.capitalize()}: {quantity} x ${price:.2f} = ${cost:.2f}")
    print(f"Total: ${total_cost:.2f}")

# Main program
print("Welcome to the supermarket!")
buy_goods()
print_receipt()