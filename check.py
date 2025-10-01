import products as db

# НЕ очищаємо базу, просто переглядаємо
all_products = db.get_all_products()

if not all_products:
    print("База порожня 😕")
else:
    print("Всі товари у базі:")
    for product in all_products:
        print(dict(product))

# Нові товари
new_products = db.get_new_products()
print("\nНові товари:")
for product in new_products:
    print(dict(product))
