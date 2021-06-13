class Beverage:
    def __init__(self, name=str()):
        self.name = name
        self.ingredientList = []  # List of IngredientQuantity (Ingredient  + Amount)

    def fromJson(self, jsonEntry):
        pass

    def __repr__(self):
        return '"%s"' % self.name
