inventory = []

class Item:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def myfunc(self):
    print(self.name)
    print(self.price)
    print(self.quantity)


class Inventory_management:
    def add_item(self,item_obj):
        inventory.append(item_obj)

    def remove_item(self,item_obj):
        inventory.remove(item_obj)
    
    def update_item(self,item_obj,update):
        pos = inventory.index(item_obj)
        inventory[pos] = update

    def display_inventory(self,inventory):
        print(inventory)
    
# njugu = Item("njugu",19 ,2)
# x = Item("tissue",20 ,1)
# x.myfunc()

system = Inventory_management()
system.display_inventory()
print(inventory)


