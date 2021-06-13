import threading
import unittest
import json

from src.VendingMachine.IngredientInSlot import IngredientInSlot
from src.VendingMachine.VendingMachineDriver import VendingMachineDriver


class CoffeeVendingTest(unittest.TestCase):
    vendingMachineDriver = VendingMachineDriver()

    def test_0_configureVendingMachine(self):
        with open("test/resources/sampleInput.json") as ingredientFile:
            sampleInput = json.load(ingredientFile)['machine']

        ingredientItems = sampleInput['total_items_quantity']
        self.vendingMachineDriver.vendingMachine.setOutletCount(sampleInput['outlets']['count_n'])
        for ingredientName in ingredientItems:
            amount = ingredientItems[ingredientName]
            ingredient = self.vendingMachineDriver.ingredientDB.getByNameOrAdd(ingredientName)
            self.vendingMachineDriver.vendingMachine.addSlot(IngredientInSlot(amount, ingredient))

        beverageItems = sampleInput['beverages']
        for beverageName in beverageItems:
            self.vendingMachineDriver.configureBeverage(beverageName, beverageItems[beverageName])

        self.assertEqual(6, self.vendingMachineDriver.getIngredientDBSize())
        self.assertEqual(4, self.vendingMachineDriver.getBeverageDBSize())

    def test_1_outletCount(self):
        print("Outlet Count: ", self.vendingMachineDriver.vendingMachine.outletCount)
        print()

    def test_2_availableBeverageTest(self):
        print("Available Beverage: ", self.vendingMachineDriver.vendingMachine.availableBeverage)
        self.assertEqual(4, len(self.vendingMachineDriver.vendingMachine.availableBeverage))
        print()

    def test_3_availableIngredientTest(self):
        print("Available Ingredients in Machine: ", self.vendingMachineDriver.vendingMachine.ingredientSlotList)
        print("Ingredients Health: ", self.vendingMachineDriver.vendingMachine.getSlotStatus())
        print()

    def test_4_refillSlotTest(self):
        print("Add Sugar Syrup amount = 40 ml")
        self.vendingMachineDriver.vendingMachine.refill(name='sugar_syrup', amount=40)
        self.test_3_availableIngredientTest()
        print()

    def test_5_getADrinkOneByOne(self):
        print("Simple Dispense test")
        print("Dispensing green_tea in from outlet 1")
        self.vendingMachineDriver.vendingMachine.dispenseFrom(outlet=1, beverageName="green_tea")
        print()

    def test_6_getDrinksParallelTest(self):
        print("Parallel test")
        testCases = [[1, 'hot_coffee'],
                     [1, 'hot_tea'],
                     [2, 'black_tea']]
        threads = []
        for test in testCases:
            threads.append(
                threading.Thread(target=self.vendingMachineDriver.vendingMachine.dispenseFrom, args=(test[0], test[1])))
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        print()


if __name__ == '__main__':
    unittest.main()
