from datetime import datetime
import threading
import time
from enum import Enum


class Indicator(Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2


class VendingMachine:
    def __init__(self):
        self.ingredientSlotList = []  # List Of Ingredients in slot with amount
        self.availableBeverage = []  # List of Beverage
        self.outletCount = int()
        self.isBusyOutlet = [False]
        self.outletLock = []

    def setOutletCount(self, outlet):
        self.outletCount = outlet
        self.isBusyOutlet = [False] * outlet
        for i in range(outlet):
            self.outletLock.append(threading.Lock())

    def addSlot(self, ingredientInSlot):
        self.ingredientSlotList.append(ingredientInSlot)

    def refill(self, name, amount):
        for ingredientItem in self.ingredientSlotList:
            if ingredientItem.ingredient.name == name:
                ingredientItem.available += amount

    def getSlotStatus(self):
        indicator = []
        for slot in self.ingredientSlotList:
            percentageAvailable = (slot.available / slot.capacity) * 100
            if percentageAvailable < 20.0:
                indicator.append((slot.ingredient.name, Indicator.RED.name))
            elif percentageAvailable < 50.0:
                indicator.append((slot.ingredient.name, Indicator.YELLOW.name))
            else:
                indicator.append((slot.ingredient.name, Indicator.GREEN.name))
        return indicator

    def getBeverageByName(self, beverageName):
        for beverage in self.availableBeverage:
            if beverage.name == beverageName:
                return beverage

    def getCurrentIngredientState(self, name):
        for ingredientItem in self.ingredientSlotList:
            if ingredientItem.ingredient.name == name:
                return ingredientItem

    def canPourBeverage(self, beverageName):
        beverage = self.getBeverageByName(beverageName)
        for requiredIngredient in beverage.ingredientList:
            availableIngredient = self.getCurrentIngredientState(requiredIngredient.ingredient.name)
            if not availableIngredient or availableIngredient.available < requiredIngredient.amount:
                return False
        return True

    def dispense(self, beverageName):
        beverage = self.getBeverageByName(beverageName)
        for requiredIngredient in beverage.ingredientList:
            self.getCurrentIngredientState(
                requiredIngredient.ingredient.name).available -= requiredIngredient.amount

    def dispenseFrom(self, outlet, beverageName):
        if not self.isBusyOutlet[outlet]:
            if self.canPourBeverage(beverageName):
                with self.outletLock[outlet]:
                    self.isBusyOutlet[outlet] = True
                    print(datetime.now().strftime("%H:%M:%S"), "Preparing: ", beverageName)
                    time.sleep(3)
                    self.dispense(beverageName)
                    print(datetime.now().strftime("%H:%M:%S"), "Prepared: ", beverageName)
                    self.isBusyOutlet[outlet] = True
            else:
                print(datetime.now().strftime("%H:%M:%S"), "Cannot Prepare: ", beverageName, "Low Ingredient")
        else:
            print(datetime.now().strftime("%H:%M:%S"), "Cannot Prepare: ", beverageName, ", outlet %s busy" % outlet)
