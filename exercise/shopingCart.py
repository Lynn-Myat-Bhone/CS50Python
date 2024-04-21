class ShoppingCart:
    def __init__(self):
        self.item = []
    
    def add(self,item_name,qty):
        item= (item_name,qty)
        self.item.append(item)
    
    def remove(self,item_name):
        for i in self.item:
            if item_name == i[0]:
                self.item.remove(i)
    
    def total (self):
        total = 0
        for i in self.item:
            total += i[1]
        return total

cart = ShoppingCart()
cart.add("Papaya", 1)
cart.add("Guava", 20)
cart.add("Orange", 15)

# Display the current items in the cart and calculate the total quantity
print("Current Items in Cart:")
for item in cart.item:
    print(item[0], "-", item[1])

total_qty = cart.total()
print("Total Quantity:", total_qty)

# Remove an item from the cart, display the updated items, and recalculate the total quantity
cart.remove("Papaya")
print("\nUpdated Items in Cart after removing Orange:")
for item in cart.item:
    print(item[0], "-", item[1])

total_qty = cart.total()
print("Total Quantity:", total_qty)             
        