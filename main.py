from vendingMachine import VendingMachine, Coin, Product

vending_machine = VendingMachine()


def buy(user_input):

    if user_input in Product.OPTIONS:
        product_option = Product.OPTIONS[user_input]
    else:
        print("Invalid Input")
        return

    can_buy = vending_machine.purchase(float(Product.PRICE[product_option]))
    if can_buy:
        print("Item Vended.")
        print("You currently have $" + str(vending_machine.get_credit()) + " left.")

    else:
        print("Not enough money.")


def add_coin(user_input):
    if user_input == "1":
        vending_machine.insert_coin(Coin(1))
    elif user_input == "0.5":
        vending_machine.insert_coin(Coin(0.50))
    elif user_input == "0.25":
        vending_machine.insert_coin(Coin(0.25))
    elif user_input == "0.1":
        vending_machine.insert_coin(Coin(0.10))
    elif user_input == "0.05":
        vending_machine.insert_coin(Coin(0.05))
    else:
        print("Invalid Input")


def main():
    switch = 1
    while switch == 1:
        print("Welcome to my Vending Machine")

        print("Here are the coin you can put!")

        print(Coin.VALUES)

        print()

        user_switch = 1
        while user_switch == 1:
            user_input = input("Please insert your coins: ").upper()
            add_coin(user_input)
            print()
            choice = 1
            while choice == 1:
                print("You currently have $" + str(vending_machine.get_credit()))
                user_input = input("Are you finished with inserting coins?(y/n): ").lower()
                if user_input == "y":
                    user_switch = 0
                    choice = 0
                    switch = 0
                elif user_input == "n":
                    user_switch = 1
                    choice = 0
                else:
                    print("Invalid command")
                    choice = 1

        print("Here are your selections!")
        for item, selection in Product.OPTIONS.items():
            print(item, selection)

        print()

        print("Here are the prices")
        for item, price in Product.PRICE.items():
            print(item, price)

        print()

        user_switch = 1
        while user_switch == 1:
            print("You currently have $" + str(vending_machine.get_credit()))
            user_input = input("Please input your selection: ").upper()
            buy(user_input)
            print()
            choice = 1
            while choice == 1:
                user_input = input("Are you finished with the vending?(y/n): ").lower()
                if user_input == "y":
                    user_switch = 0
                    choice = 0
                    switch = 0
                elif user_input == "n":
                    user_switch = 1
                    choice = 0
                else:
                    print("Invalid command")
                    choice = 1

        print("Get your remaining money $" + str(vending_machine.get_credit()))
        print("Thank you for using this vending machine")


main()
