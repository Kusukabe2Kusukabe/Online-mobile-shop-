# Sample mobile products in the shop
products = {
    1: {"name": "iPhone 14", "description": "Latest model with 128GB storage", "price": 999.99, "stock": 10},
    2: {"name": "Samsung Galaxy S23", "description": "Flagship model with 256GB storage", "price": 899.99, "stock": 15},
    3: {"name": "Google Pixel 7", "description": "Android with excellent camera", "price": 699.99, "stock": 20},
    4: {"name": "OnePlus 11", "description": "Fast charging with 256GB storage", "price": 749.99, "stock": 5}
}

# Cart to store user's selection
cart = {}

# Main loop to handle user input
while True:
    print("\n--- Welcome to the Online Mobile Shop ---")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")
    
    # Get user's choice
    choice = input("Please choose an option (1-5): ")

    if choice == "1":
        # View Products
        print("\nAvailable Products:")
        for product_id, product_info in products.items():
            print(f"{product_id}. {product_info['name']}: {product_info['description']}")
            print(f"   Price: ${product_info['price']} | Stock: {product_info['stock']}\n")

    elif choice == "2":
        # Add Product to Cart
        try:
            product_id = int(input("Enter the product ID to add to your cart: "))
            if product_id in products:
                quantity = int(input(f"Enter quantity for {products[product_id]['name']}: "))
                if quantity > 0 and quantity <= products[product_id]["stock"]:
                    if product_id in cart:
                        cart[product_id]["quantity"] += quantity
                    else:
                        cart[product_id] = {"name": products[product_id]["name"], "price": products[product_id]["price"], "quantity": quantity}
                    products[product_id]["stock"] -= quantity  # Decrease stock
                    print(f"Added {quantity} x {products[product_id]['name']} to your cart.")
                else:
                    print("Invalid quantity! Not enough stock.")
            else:
                print("Invalid product ID.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        # View Cart
        if cart:
            print("\nYour Cart:")
            total_price = 0
            for product_id, item in cart.items():
                print(f"{item['name']} - {item['quantity']} x ${item['price']} = ${item['quantity'] * item['price']}")
                total_price += item['quantity'] * item['price']
            print(f"\nTotal: ${total_price:.2f}")
        else:
            print("\nYour cart is empty.")

    elif choice == "4":
        # Checkout
        if cart:
            total_price = 0
            print("\nCheckout Summary:")
            for product_id, item in cart.items():
                print(f"{item['name']} - {item['quantity']} x ${item['price']} = ${item['quantity'] * item['price']}")
                total_price += item['quantity'] * item['price']
            print(f"\nTotal Amount: ${total_price:.2f}")
            proceed = input("Do you want to proceed to payment? (yes/no): ").lower()
            if proceed == "yes":
                print("Payment successful. Thank you for shopping with us!")
                cart.clear()  # Clear the cart after successful checkout
            else:
                print("Checkout canceled.")
        else:
            print("\nYour cart is empty. Add some products to your cart first.")

    elif choice == "5":
        print("Thank you for visiting our shop! Goodbye.")
        break

    else:
        print("Invalid choice. Please choose again.")
