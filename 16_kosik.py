# 16_kosik.py

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        """Adds an item to the cart."""
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name):
        """Removes an item from the cart by name."""
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                break
        else:
            print(f"Item '{name}' not found in the cart.")

    def calculate_total(self):
        """Calculates the total amount of the cart."""
        total = sum(item["price"] * item["quantity"] for item in self.items)
        return total

    def print_invoice(self):
        """Prints an invoice for the cart."""
        if not self.items:
            print("The cart is empty.")
            return
        
        print("Invoice:")
        print("----------------------------")
        for item in self.items:
            print(f"{item['quantity']}x {item['name']} - {item['price']} Kč")
        
        print("----------------------------")
        print(f"Total amount: {self.calculate_total()} Kč")
        print("----------------------------")


# Example usage
if __name__ == "__main__":
    cart = Cart()
    
    # Add items to the cart
    cart.add_item("Headphones", 1500, 1)
    cart.add_item("Smartphone", 1200, 1)
    cart.add_item("Sofa", 800, 1)
    cart.add_item("Postcards", 3, 3)
    
    # Remove an item
    cart.remove_item("Postcards")
    
    # Print the invoice
    cart.print_invoice()
