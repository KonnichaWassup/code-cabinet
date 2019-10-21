import random

BasketNumber = 0
CheckoutBasket = []


class FruitClass:
    def __init__(self, Name, Color, Taste):
        self.Name = Name
        self.Taste = Taste
        self.Color = Color


lemon = FruitClass('Lemon', 'yellow', 'sour')
apple = FruitClass('Apple', 'red', 'sweet')
avocado = FruitClass('Avocado', 'green', 'sweet')
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
    while BasketNumber > 0:
        randomfruit = random.choice(FruitBasket)
        BasketNumber = BasketNumber - 1
        CheckoutBasket.append(randomfruit)
    else:
        pass

    for fruit in CheckoutBasket:
        print("Added a " + fruit.Color + " " + fruit.Name + " to the checkout basket!" + " Looks " + fruit.Taste + "!")


start()
randompick()




