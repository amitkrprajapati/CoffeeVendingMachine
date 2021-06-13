class BeverageDB:
    def __init__(self):
        self.beverages = []  # List of IngredientQuantity

    def add(self, beverage):
        self.beverages.append(beverage)
