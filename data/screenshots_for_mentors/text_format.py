from catalog.models import Category, Product


category1 = Category.objects.create(name="Категория 1", description="Описание 1")
category2 = Category.objects.create(name="Категория 2", description="Описание 2")
category3 = Category.objects.create(name="Категория 3", description="Описание 3")

product1 = Product.objects.create(name="Продукт 1", category=category1, price=100.10, description="Описание 1")
product2 = Product.objects.create(name="Продукт 1", category=category1, price=200.20, description="Описание 2")
product3 = Product.objects.create(name="Продукт 2", category=category1, price=300.30, description="Описание 3")
product4 = Product.objects.create(name="Продукт 3", category=category1, price=400.40, description="Описание 4")
product5 = Product.objects.create(name="Продукт 3", category=category1, price=500.50, description="Описание 5")

categories = Category.objects.all()
for category in categories:
    print(category)

products = Product.objects.all()
for product in products:
    print(product)

products_filter = Product.objects.filter(category_id=3)
for product in products_filter:
    print(product)

product_price_change = Product.objects.get(name="Продукт 2")
product_price_change.price = 222.22
product_price_change.save()
product_price_change = Product.objects.get(name="Продукт 2")
print(product_price_change)

product_delete = Product.objects.get(name="Продукт 4")
product_delete.delete()

all_product = Product.objects.all()
for product in all_product:
    print(product)
