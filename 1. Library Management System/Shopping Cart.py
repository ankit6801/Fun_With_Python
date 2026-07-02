class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        print("Cart:", self.items)


cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("Mouse")

cart.show_items()
#Ankit Kumar