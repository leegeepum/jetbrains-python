class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.status = ''

    def write_action(self):
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        self.status = action
        return self.status

    def action_buy(self):
        buy = input("What do you want to buy? 1 - espresso, 2 - latte, "
                    "3 - cappuccino, back - to main menu:\n")
        if buy == '1':
            if self.water // 250 < 1 or self.beans // 16 < 1:
                print("Sorry, not enough water!\n")
            else:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
        elif buy == '2':
            if self.water // 350 < 1 or self.milk // 75 < 1 or self.beans // 20 < 1:
                print("Sorry, not enough water!\n")
            else:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
        elif buy == '3':
            if self.water // 200 < 1 or self.milk // 100 < 1 or self.beans // 12 < 1:
                print("Sorry, not enough water!\n")
            else:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1

    def action_fill(self):
        fill_water = int(input("Write how many ml of water do you want to add:\n"))
        fill_milk = int(input("Write how many ml of milk do you want to add:\n"))
        fill_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        fill_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.water += fill_water
        self.milk += fill_milk
        self.beans += fill_beans
        self.cups += fill_cups
        print()

    def action_take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        print()

    def action_remaining(self):
        print(f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money""")

coffeemachine = CoffeeMachine()

while coffeemachine.write_action() != 'exit':
    print()
    if coffeemachine.status == 'remaining':
        coffeemachine.action_remaining()
        print()
    elif coffeemachine.status == 'buy':
        coffeemachine.action_buy()
        print()
    elif coffeemachine.status == 'fill':
        coffeemachine.action_fill()
    elif coffeemachine.status == 'take':
        coffeemachine.action_take()
