import random
import sys

CheckoutBasket = []


class FruitClass:
    def __init__(self, Name, Color, Taste, Cost):
        self.Name = Name
        self.Taste = Taste
        self.Color = Color
        self.Cost = Cost


lemon = FruitClass('Lemon', 'yellow', 'sour', 1)
apple = FruitClass('Apple', 'red', 'sweet', 2)
avocado = FruitClass('Avocado', 'green', 'sweet', 3)
watermelon = FruitClass('Watermelon', 'green', 'sweet', 4)
fruitbasket = [lemon, apple, avocado, watermelon]


def startrandom(budget):

    while True:
        addrandom = str(input("Add random fruits to the basket? (please type 'y' or 'n')\n"))
        if addrandom == "y":
            pass
        else:
            if addrandom == "n":
                sys.exit("Exit.")
            if addrandom != "y" or "n":
                print("Invalid input.")

        try:
            budget = int(input("Enter available funds: "))
            print("Entered $" + str(budget))
            if budget == 0:
                print("Please enter a value greater than zero.")
            else:
                pass
        except ValueError:
            print("Please type a number.")
        return budget


def randompick(limit, total):

    while total < limit:

        randomfruit = random.choice(fruitbasket)
        CheckoutBasket.append(randomfruit)
        total = total + randomfruit.Cost

        print(
            "Added a " + randomfruit.Color + " " + randomfruit.Name + " to the checkout basket!" + " Looks " +
            randomfruit.Taste + "! " + "Costs $" + str(randomfruit.Cost) + ". Total Cost: " + str(total) + "."
        )

        if limit - total == 1:
            try:
                fruitbasket.remove(apple)
                fruitbasket.remove(avocado)
                fruitbasket.remove(watermelon)
            except ValueError:
                pass
        if limit - total == 2:
            try:
                fruitbasket.remove(avocado)
                fruitbasket.remove(watermelon)
            except ValueError:
                pass
        if limit - total == 3:
            fruitbasket.remove(watermelon)
    else:
        return None


x = 0
y = 0
x = startrandom(x)
randompick(x, y)
