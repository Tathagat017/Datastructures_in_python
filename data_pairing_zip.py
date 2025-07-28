products = ["Laptop", "Smartphone", "Tablet","Smartwatch"]
prices = [1000, 800, 600, 300]
quantities = [5, 10, 15, 20]

products_prices = []
for product,price in zip(products, prices):
    products_prices.append((product, price))
    
product_prices = []
for product,price,quantity in zip(products, prices, quantities):
    product_prices.append((price*quantity))
    
print("Products with their prices:", products_prices)
    
total_price_for_products = sum(product_prices)

print("Total price for all products:", total_price_for_products)

product_cataloug = {}

for product, price, quantity in zip(products, prices, quantities):
    product_cataloug[product] = {
        "price": price, 
        "quantity": quantity,
        "total_value": price * quantity
    }

low_stock_products = []
for produtc, details in product_cataloug.items():
    if(details["quantity"] < 10):
        low_stock_products.append(produtc)
      
  
print("Low stock products:", low_stock_products)      