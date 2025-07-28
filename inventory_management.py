


class ProductDetails:
    def __init__(self,quantity,price):
        self.quantity = quantity
        self.price_per_unit = price

class Product:
    def _init__(self,name:str,details:ProductDetails):
        self.name = name 
        self.details = details
        

class InventoryManagement:
    inventory = []
    
    def _init__(self):
        pass
    
    @classmethod
    def add_product(cls, name: str, quantity: int, price_per_unit: float):
        product_details = ProductDetails(quantity, price_per_unit)
        product = Product(name, product_details)
        cls.inventory.append(product)
        print(f"Added {name} to inventory with quantity {quantity} and price per unit {price_per_unit}")
        
    @classmethod
    def remove_product(cls, name: str):
        for product in cls.inventory:
            if product.name == name:
                cls.inventory.remove(product)
                print(f"Removed {name} from inventory")
                return
        print(f"{name} not found in inventory")
        
    @classmethod
    def update_product(cls, name: str, quantity: int = None, price_per_unit: float = None):
        for product in cls.inventory:
            if product.name == name:
                if quantity is not None:
                    product.details.quantity = quantity
                if price_per_unit is not None:
                    product.details.price_per_unit = price_per_unit
                print(f"Updated {name} in inventory")
                return
        print(f"{name} not found in inventory")
        
    @classmethod
    def display_inventory(cls):
        if not cls.inventory:
            print("Inventory is empty")
            return
        print("Current Inventory:")
        for product in cls.inventory:
            print(f"{product.name}: Quantity = {product.details.quantity}, Price per unit = {product.details.price_per_unit}")
        
        
        