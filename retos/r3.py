# Array de categorías
categories = [
    {"id": 1, "name": "Electrónicos"},
    {"id": 2, "name": "Ropa"},
    {"id": 3, "name": "Hogar"},
    {"id": 4, "name": "Alimentación"},
]

# Array de productos
products = [
    {"id": 1, "name": "Televisor LED 50 pulgadas", "price": 599.99, "category_id": 1},
    {"id": 2, "name": "Camiseta de algodón", "price": 19.99, "category_id": 2},
    {"id": 3, "name": "Sartén antiadherente", "price": 34.99, "category_id": 3},
    {"id": 4, "name": "Manzanas (1 kg)", "price": 2.49, "category_id": 4},
]


# Forma 1:
data = []

for category in categories:
    for product in products:
        if category['id'] == product['category_id']:
            product.update({'category': category['name']})
            data.append(product)

print(data)

# Forma 2:
for product in products:
    product.update({'category': category['name'] for category in categories if category['id'] == product['category_id']})
    
[print(item) for item in products]
