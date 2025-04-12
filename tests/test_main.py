from src.main import Product, Category

def test_product_init(product, product1, product2, product3):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

    assert product1.name == "Iphone 15"
    assert product1.description == "512GB, Gray space"
    assert product1.price == 210000.0
    assert product1.quantity == 8

    assert product2.name == "Xiaomi Redmi Note 11"
    assert product2.description == "1024GB, Синий"
    assert product2.price == 310000.0
    assert product2.quantity == 14

    assert product3.name == '55" QLED 4K'
    assert product3.description == "Фоновая подсветка"
    assert product3.price == 123000.0
    assert product3.quantity == 7


def test_category_init(category1, category2):
    assert category1.name == "Смартфоны"
    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )


    assert category1.category_count == 2
    assert category2.category_count == 2

    assert category1.product_count == 1
    assert category2.product_count == 1




def test_product_creation(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 1000
    assert sample_product.quantity == 10


def test_product_price_setter_increase(sample_product):
    sample_product.price = 1200
    assert sample_product.price == 1200


def test_product_price_setter_decrease(sample_product, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    sample_product.price = 800
    assert sample_product.price == 800


def test_product_price_setter_decrease_cancel(sample_product, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    sample_product.price = 800
    assert sample_product.price == 1000  # Цена не должна измениться


def test_product_price_setter_negative(sample_product, capsys):
    sample_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 1000  # Цена не должна измениться


def test_category_creation(sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert "Test Product, 1000 руб. Остаток: 10 шт." in sample_category.products


def test_category_add_product(sample_category):
    new_product = Product("New Product", "New Description", 500, 5)
    sample_category.add_product(new_product)
    assert "New Product, 500 руб. Остаток: 5 шт." in sample_category.products
    assert Category.product_count == 2


def test_category_products_getter(sample_category):
    expected_output = "Test Product, 1000 руб. Остаток: 10 шт."
    assert expected_output in sample_category.products


def test_category_multiple_products():
    product1 = Product("Product 1", "Description 1", 1000, 5)
    product2 = Product("Product 2", "Description 2", 2000, 3)
    category = Category("Test Category", "Test Description", [product1, product2])

    expected_output1 = "Product 1, 1000 руб. Остаток: 5 шт."
    expected_output2 = "Product 2, 2000 руб. Остаток: 3 шт."
    assert expected_output1 in category.products
    assert expected_output2 in category.products


def test_new_product_creation():
    product_dict = {
        "name": "New Product",
        "description": "New Description",
        "price": 1500,
        "quantity": 7
    }
    new_product = Product.new_product(product_dict)
    assert new_product.name == "New Product"
    assert new_product.description == "New Description"
    assert new_product.price == 1500
    assert new_product.quantity == 7


def test_new_product_duplicate():
    Product.products = []  # Очищаем список продуктов перед тестом
    product_dict = {
        "name": "Duplicate Product",
        "description": "Description",
        "price": 1000,
        "quantity": 5
    }
    Product.new_product(product_dict)
    duplicate = Product.new_product(product_dict)
    assert len(Product.products) == 0
    assert duplicate.quantity == 5  # Количество должно суммироваться
