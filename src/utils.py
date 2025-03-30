import json
import os

from src.main import Category, Product


def read_json(path: str) -> dict:
    """Функция загружает данные из json-файла и преобразует их в объкт Python."""

    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF=8") as file:
        data = json.load(file)
    return data


def create_class_objects_from_json(data):
    """Функциональность загрузки данных из JSON-файла для наполнения каталога."""

    class_objects = []
    for object in data:
        products = []
        for product in object["products"]:
            products.append(Product(**product))
        object["products"] = products
        class_objects.append(Category(**object))

    return class_objects


if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, "..", "data")
    json_file_path = os.path.join(data_dir, "product.json")
    gadgets = read_json(json_file_path)
    object_gadgets = create_class_objects_from_json(gadgets)
    print(object_gadgets)

