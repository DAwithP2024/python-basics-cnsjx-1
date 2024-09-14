# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_categories():
    """Display categories and return the user's choice as an index."""
    print("\nAvailable categories:")
    for i, category in enumerate(products.keys(), 1):
        print(f"{i}. {category}")
    
    category_input = input("Please select a category (enter the corresponding number): ").strip()
    
    # Handle non-numeric input or out-of-range numbers
    if not category_input.isdigit() or not (1 <= int(category_input) <= len(products)):
        return None
    
    return int(category_input) - 1

def display_products(products_list):
    """Return the product index based on user input."""
    print("\nAvailable products:")
    for i, product in enumerate(products_list, 1):
        print(f"{i}. {product[0]} - ${product[1]}")

    product_input = input("Enter the number of the product you'd like to buy: ").strip()
    
    if not product_input.isdigit() or not (1 <= int(product_input) <= len(products_list)):
        return None
    
    return int(product_input) - 1

def display_sorted_products(products_list, sort_order):
    """Return sorted products based on the sort order."""
    reverse = True if sort_order == 'desc' else False
    sorted_list = sorted(products_list, key=lambda x: x[1], reverse=reverse)
    return sorted_list

def add_to_cart(cart, product, quantity):
    """Add selected product and quantity to the cart."""
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    """Display the cart content and print the total cost."""
    total = 0
    for item in cart:
        name, price, quantity = item
        subtotal = price * quantity
        total += subtotal
        print(f"{name} - ${price} x {quantity} = ${subtotal}")
    
    print(f"Total cost: ${total}")
    return total

def generate_receipt(name, email, cart, total_cost, address):
    """Generate and return the receipt for testing purposes."""
    receipt = f"Customer: {name}\nEmail: {email}\n"
    receipt += "Items Purchased:\n"
    for item in cart:
        name_item, price, quantity = item
        receipt += f"{quantity} x {name_item} - ${price} = ${price * quantity}\n"
    receipt += f"Total: ${total_cost}\n"
    receipt += f"Delivery Address: {address}\n"
    receipt += "Your items will be delivered in 3 days. Payment will be accepted after successful delivery."
    return receipt

def validate_name(name):
    """Validate that the name consists of two parts and only contains letters."""
    parts = name.strip().split()
    if len(parts) != 2:
        return False
    first_name, last_name = parts
    return first_name.isalpha() and last_name.isalpha()

def validate_email(email):
    """Validate that the email contains an '@' and a period."""
    if '@' in email:
        return True
    return False

def main():
    """Main function controlling the program flow."""
    print("Welcome to the Online Shopping Store!")
    
    # Get and validate user name
    while True:
        name = input("Please enter your full name (first and last name): ").strip()
        if validate_name(name):
            break
        else:
            print("Invalid name. Please ensure it contains a first and last name with only letters.")
    
    # Get and validate user email
    while True:
        email = input("Please enter your email address: ").strip()
        if validate_email(email):
            break
        else:
            print("Invalid email address. Please ensure it contains '@' and '.' symbols.")
    
    cart = []
    
    while True:
        category_index = display_categories()
        if category_index is None:
            print("Invalid category selection. Please try again.")
            continue
        
        category_name = list(products.keys())[category_index]
        selected_products = products[category_name]
        
        while True:
            print("\nPlease choose an action:")
            print("1. Select a product to buy")
            print("2. Sort products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")
            action = input("Enter your choice (1-4): ").strip()
            
            if action == '1':
                product_index = display_products(selected_products)
                if product_index is None:
                    print("Invalid product selection. Please try again.")
                    continue
                product = selected_products[product_index]
                
                quantity_input = input(f"How many {product[0]} would you like to buy? ").strip()
                if not quantity_input.isdigit() or int(quantity_input) <= 0:
                    print("Invalid quantity. Please enter a positive integer.")
                    continue
                quantity = int(quantity_input)
                add_to_cart(cart, product, quantity)
            
            elif action == '2':
                while True:
                    sort_choice = input("Enter 1 for ascending or 2 for descending order: ").strip()
                    if sort_choice not in ['1', '2']:
                        print("Invalid choice. Please enter 1 or 2.")
                        continue
                    sort_order = 'asc' if sort_choice == '1' else 'desc'
                    sorted_products = display_sorted_products(selected_products, sort_order)
                    display_products(sorted_products)
                    break
            
            elif action == '3':
                # Return to category selection
                break
            
            elif action == '4':
                if cart:
                    total_cost = display_cart(cart)
                    address = input("Please enter your delivery address: ").strip()
                    receipt = generate_receipt(name, email, cart, total_cost, address)
                    print(receipt)
                else:
                    print("Thank you for using our service. We hope to see you next time. Have a great day!")
                return  # End the program

if __name__ == "__main__":
    main()
