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


def test_category_init(category1, category2, category3):
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
    assert len(category1.products) == 3
    assert len(category2.products) == 1
    assert len(category3.products) == 4

    assert category1.category_count == 3
    assert category2.category_count == 3
    assert category3.category_count == 3

    assert category1.product_count == 4
    assert category2.product_count == 4
    assert category3.product_count == 4
    assert category2.products[0].name == '55" QLED 4K'
    assert category2.products[0].description == "Фоновая подсветка"
    assert category2.products[0].price == 123000.0
    assert category2.products[0].quantity == 7
