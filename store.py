store = {"Laptop":{"Price":1200, "Quantity":5},
        "Headphones":{"Price":150, "Quantity":10},
        "Mouse":{"Price":40, "Quantity":20}
        }
def add_product(store, name, price, quantity):
    store[name.capitalize()]={"Price":price, "Quantity":quantity}
def update_stock(store, name, quantity):
    store[name.capitalize()]["Quantity"]=quantity
def sell_product(store, name, quantity):
    if quantity<=store[name.capitalize()]["Quantity"]:
        cost=store[name.capitalize()]["Price"]*quantity
        store[name.capitalize()]["Quantity"]-=quantity
        new_quantity=store[name.capitalize()]["Quantity"]
        print(f"The total cost is {cost} and the new quantity is {new_quantity}")
    else:
        short=quantity-store[name.capitalize()]["Quantity"]
        print(f"Sorry, we are short of the product by {short}")
running = True
while running:
    print("Welcome to the store")
    command = int(input('''
    press the number of the operation you want to perform
    1. Add a new product
    2. Update existing stock
    3. Make a sale
    4. Display inventory
    5. Find most expensive product
    6. Find total value of inventory
    0. Exit
    What do you want to do: '''))
    if command ==0:
        running = False
    elif command ==1:
        name=input("What do you want to add? ")
        if name.capitalize() not in store.keys():
            quantity=int(input("How many do you want to add? "))
            price= int(input("What is the price of a single unit? "))
            add_product(store, name, price, quantity)
            print("Item succesfully added")
        else:
            print("Item already exists")
    elif command ==2:
        name=input("What do you want to update? ")
        if name.capitalize() in store.keys():
            quantity=int(input("What is the new amount? "))
            update_stock(store, name, quantity)
            print(store)
        else:
            print("item does not exist")
    elif command ==3:
        name=input("What do you want to sell? ")
        if name.capitalize() in store.keys():
            quantity=int(input("How many does the customer want to buy? "))
            sell_product(store, name, quantity)
        else:
            print("Item does not exist in inventory? ")







print("Goodbye have a nice day")

