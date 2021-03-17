import sqlite3
import random

# create Class BankAccount
class BankAccount:

    # create parameters
    def __init__(self):
        self.program = ''
        self.account_num = ''
        self.logged_in_account = ''
        self.pin_create = []
        self.pin_num = ''
        self.pin_input = ''
        self.balance = 0
        self.added_income = 0
        self.programmes = False
        self.conn = sqlite3.connect('card.s3db')
        self.c = self.conn.cursor()
        self.transfer_destination = ''
        self.transfer_amount = 0

    def drop_table(self):
        self.c.execute("DROP TABLE IF EXISTS card;")
        self.conn.commit()

    def create_table(self):
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)")
        self.conn.commit()

    def insert_data(self):
        self.c.execute(f"INSERT INTO card (number, pin) VALUES ({self.account_num}, {self.pin_num})")
        self.c.execute(f"SELECT * FROM card")
        print(self.c.fetchall())
        self.conn.commit()

    def return_data(self):
        self.c.execute("SELECT * FROM card")
        self.conn.commit()
        return self.c.fetchall()

    def add_income(self):
        self.c.execute(f"UPDATE card SET balance = {self.added_income} + {self.balance} WHERE number = '{self.logged_in_account}'")
        self.c.execute("SELECT * FROM card")
        # print(self.c.fetchall())
        self.conn.commit()

    def transfer(self):
        self.c.execute(f"UPDATE card SET balance = {self.transfer_amount} WHERE number = '{self.transfer_destination}'")
        self.c.execute(f"UPDATE card SET balance = {self.balance - self.transfer_amount}")
        self.c.execute("SELECT * FROM card")
        print(self.c.fetchall())
        self.conn.commit()

    def delete(self):
        self.c.execute(F"DELETE FROM card WHERE number = '{self.logged_in_account}'")
        self.c.execute(f"SELECT * FROM card")
        print(self.c.fetchall())
        self.conn.commit()

    # start the initial program
    def program_start(self):
        self.program = input("1. Create an account\n"
                                "2. Log into account\n"
                                "0. Exit\n")
        return self.program

    # create initial account
    def create_account(self):

        # set local variables
        id_num = '400000'
        account_create = []
        integer_account_luhn = []
        pin_create = []
        account_checksum = 0

        # create the last 9 random account numbers
        for i in range(9):
            i = random.randint(0, 9)
            account_create.append(str(i))
        self.account_num = id_num + ''.join(account_create)
        account_luhn = list(self.account_num)

        # concatenate the first and last parts of account numbers
        for i in range(len(account_luhn)):
            integer_account_luhn.append(int(account_luhn[i]))

        # transform the account number following the luhn rules
        for i in range(len(integer_account_luhn)):
            if (i + 1) % 2 == 1:
                integer_account_luhn[i] = integer_account_luhn[i] * 2
            if integer_account_luhn[i] > 9:
                integer_account_luhn[i] -= 9
        # print(integer_account_luhn)

        # create a checksum number
        if sum(integer_account_luhn) % 10 != 0:
            account_checksum = 10 - (sum(integer_account_luhn) % 10)
        self.account_num += str(account_checksum)

        # create initial pin number
        for i in range(4):
            i = random.randint(0, 9)
            pin_create.append(str(i))
            self.pin_num = ''.join(pin_create)

        # print the account information
        print(f"""
Your card has been created
Your card number:
{self.account_num}
Your card PIN:
{self.pin_num}
""")

    # transfer money
    def do_transfer(self):

        self.transfer_destination = input("\nTransfer\nEnter card number:\n")
        l_transfer_destination = list(self.transfer_destination)
        step1 = [int(i) for i in l_transfer_destination]
        step2 = step1[0:len(step1) - 1]
        step3 = [y * 2 if (x + 1) % 2 > 0 else y for x, y in enumerate(step2)]
        step4 = [x - 9 if x > 9 else x for x in step3]
        step5 = 10 - (sum(step4) % 10)
        num_l_transfer_destination = sum(step4) + step5

        print([i for i in self.return_data()])

        if self.transfer_destination == self.logged_in_account:
            print("You can't transfer money to the same account!")
        elif num_l_transfer_destination % 10 != 0 or self.transfer_destination == '4000003972196502':
            print("Probably you made a mistake in the card number. Please try again!")
        elif self.transfer_destination not in [y for x, y, z, f in self.return_data()]:
            print("Such a card does not exist.")
        else:
            self.transfer_amount = int(input("Enter how much money you want to transfer:\n"))
            if self.transfer_amount > self.balance:
                print("Not enough money!")
            else:
                print("Success!")
                print(self.transfer())
                # return self.transfer()

    # initial log in
    def log_in(self):

        # check the account information
        self.logged_in_account = input("\nEnter your card number:\n")
        self.pin_input = input("Enter your PIN:\n")

        if self.logged_in_account not in [y for x, y, z, f in self.return_data()] or self.pin_input not in [z for x, y, z, f in self.return_data()]:
            print(y, z)
            print("\nWrong card number of PIN!\n")
        else:
            print("\nYou have successfully logged in!")

            # if successfully logged in, give more options
            while True:
                login_window = input("""
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
""")
                # while logged in, show balance
                if login_window == '1':
                    print(f"\nBalance: {self.balance}")

                elif login_window == '2':
                    self.added_income = int(input("\nEnter income:\n"))
                    self.add_income()
                    self.balance += self.added_income
                    print("Income was added!")

                elif login_window == '3':
                    self.do_transfer()

                elif login_window == '4':
                    self.delete()
                    print(f"Your account {self.logged_in_account} has been deleted!")

                # while logged in, log out
                elif login_window == '5':
                    print("\nYou have successfully logged out!\n")
                    return False

                # completely exit out of the program
                else:
                    self.programmes = True
                    return False


# create an instance of bank system
bank_system = BankAccount()

bank_system.drop_table()

# running the whole program
while bank_system.programmes == False:
    # initially start the program
    bank_system.program_start()
    bank_system.create_table()

    # option 1 - create an initial account
    if bank_system.program == '1':
        bank_system.create_account()
        bank_system.insert_data()
        # for i in bank_system.return_data():
        #     print(i)

    # option 2 - log in with account info
    elif bank_system.program == '2':
        bank_system.log_in()

    # option 3 - completely exit out of program
    else:
        print("\nBye!")
        bank_system.programmes = True
