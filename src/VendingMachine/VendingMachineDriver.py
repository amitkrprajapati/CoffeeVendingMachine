from src.Beverages.BeveargeDB import BeverageDB
from src.Beverages.Beverage import Beverage
from src.Ingredients.IngredientDB import IngredientDB
from src.Ingredients.IngredientQuantity import IngredientQuantity
from src.VendingMachine.VendingMachine import VendingMachine


class VendingMachineDriver:
    vendingMachine = VendingMachine()
    ingredientDB = IngredientDB()
    beverageDB = BeverageDB()

    def configureBeverage(self, name, beverageConfiguration):
        beverage = Beverage(name)
        for ingredientName in beverageConfiguration:
            ingredientForBeverage = IngredientQuantity()
            ingredientForBeverage.ingredient = self.ingredientDB.getByNameOrAdd(ingredientName)
            ingredientForBeverage.amount = beverageConfiguration[ingredientName]

            beverage.ingredientList.append(ingredientForBeverage)
        self.beverageDB.add(beverage)
        self.vendingMachine.availableBeverage.append(beverage)

    def getIngredientDBSize(self):
        return len(self.ingredientDB.ingredients)

    def getBeverageDBSize(self):
        return len(self.beverageDB.beverages)
