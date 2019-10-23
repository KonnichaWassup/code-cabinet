import random

BasketNumber = 0
TotalCost = 0
CheckoutBasket = []


class FruitClass:
    def __init__(self, Name, Color, Taste, Cost):
        self.Name = Name
        self.Taste = Taste
        self.Color = Color
        self.Cost = Cost


lemon = FruitClass('Lemon', 'yellow', 'sour', 1)
apple = FruitClass('Apple', 'red', 'sweet', 1)
avocado = FruitClass('Avocado', 'green', 'sweet', 2)
watermelon = FruitClass('Watermelon', 'green', 'sweet', 3)
FruitBasket = [lemon, apple, avocado]

def start():
    global BasketNumber
    while True:
        try:
            BasketNumber = int(input("How many fruits?"))
        except ValueError:
            print("Enter a number!")
        else:
            print(BasketNumber)
            break


def randompick():
    global BasketNumber
    global CheckoutBasket
    global TotalCost
    while BasketNumber > 0 and TotalCost <= 10:
        randomfruit = random.choice(FruitBasket)
        # BasketNumber = BasketNumber - 1
        CheckoutBasket.append(randomfruit)
        TotalCost = TotalCost + randomfruit.Cost
        if TotalCost >= 10:
            break



    for fruit in CheckoutBasket:
        print("Added a " + fruit.Color + " " + fruit.Name + " to the checkout basket!" + " Looks " + fruit.Taste + "!")
    print(TotalCost)


start()
randompick()
