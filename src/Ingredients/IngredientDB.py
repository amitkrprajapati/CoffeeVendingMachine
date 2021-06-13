from src.Ingredients.Ingredient import Ingredient


class IngredientDB:
    def __init__(self):
        self.ingredients = []

    def fromJson(self, ingredients):
        if ingredients:
            for name in ingredients:
                self.ingredients.append(Ingredient(name))

    def getByName(self, name):
        for ingredient in self.ingredients:
            if ingredient.name == name:
                return ingredient
        return None

    def getByNameOrAdd(self, name):
        ingredient = self.getByName(name)
        if not ingredient:
            ingredient = Ingredient(name)
            self.ingredients.append(ingredient)
        return ingredient
