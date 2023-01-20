class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)
        return self.products

    def get_by_letter(self, first_letter: str):
        return [item for item in self.products if item.startswith(first_letter)]

    def __repr__(self):
        items = "\n".join(sorted(self.products))
        return f"Items in the {self.name} catalogue:" + "\n" + items


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)