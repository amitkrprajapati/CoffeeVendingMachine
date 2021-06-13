from src.Ingredients.Ingredient import Ingredient


class IngredientInSlot:
    def __init__(self, available=float(), ingredient=Ingredient()):
        self.capacity = 500  # HardCoding for now
        self.available = available
        self.ingredient = ingredient

    def __repr__(self):
        return str([self.ingredient.name, self.available])
