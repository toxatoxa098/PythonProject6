class Product:
    name: str
    description: str
    price: float
    quantity: int
    Product = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirm = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {value}? (y/n): ")
            if confirm.lower() == 'y':
                self.__price = value
                print(f"Цена успешно изменена на {value}")
            else:
                print("Изменение цены отменено")
        else:
            self.__price = value
            print(f"Цена успешно изменена на {value}")

    @classmethod
    def new_product(cls, product_dict):
        new_name = product_dict.get('name')
        new_price = product_dict.get('price')
        new_description = product_dict.get('description')
        new_quantity = product_dict.get('quantity')

        for product in cls.Product:
            if product.name.lower() == new_name.lower():
                product.quantity += new_quantity
                product.price = max(product.price, new_price)
                return product

        return cls(new_name, new_description, new_price, new_quantity)

class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count = len(products) if products else 0

    @property
    def products(self):
        new_str_product = ''
        for product in self.__products:
            new_str_product += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return new_str_product

    def add_product(self, product):
        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1



if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)
    print()

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)


    print(category1.name == "Смартфоны")
    print(category1.name)
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)
    print()

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )


    print(product4.name)
    print(product4.description)
    print(product4.price)
    print(product4.quantity)

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
