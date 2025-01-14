class Category:
    def __init__(self, name: str):
        self.name = name


class Brand:
    def __init__(self, name: str):
        self.name = name


class Product:
    def __init__(self, name: str, brand: Brand, category: Category, price: float, stock: int):
        self.name = name
        self.brand = brand
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} ({self.brand.name}) - {self.category.name}: {self.price} Kč, skladem: {self.stock}"


# Příklady kategorií
category_clothing = Category("Oblečení")
category_electronics = Category("Elektronika")

# Příklady značek
brand_puma = Brand("Puma")
brand_sony = Brand("Sony")

# Příklady produktů
hoodie = Product("Mikina", brand_puma, category_clothing, 890, 10)
headphones = Product("Sluchátka X900", brand_sony, category_electronics, 1290, 2)

# Test vypisu produktů
print(hoodie)
print(headphones)
