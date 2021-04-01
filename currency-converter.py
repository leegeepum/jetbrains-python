import json
import requests

statement = True
my_currency_code = input().lower()

class ExchangeCurrency:

    def __init__(self) -> None:

        self.url = f"http://www.floatrates.com/daily/{my_currency_code}.json"
        self.r = requests.get(self.url)
        self.currency = json.loads(self.r.content)
        self.currency_list = ['usd', 'eur']

    def currency_cache(self):

        # self.exchange_currency_code = input().lower()
        # self.currency_ammount = float(input())

        print("Checking the cache...")

        if exchange_currency_code not in self.currency_list:

            print("Sorry, but it is not in the cache!")

            self.currency_list.append(exchange_currency_code)
            self.currency_exchange = self.currency[exchange_currency_code]
            self.exchange_rate = float(self.currency_exchange['rate'])
            self.exchange_amount = round(self.exchange_rate * currency_ammount, 2)

            print(f"You received {self.exchange_amount} {exchange_currency_code.upper()}")

        else:

            print("Oh! It is in the cache!")

            self.currency_exchange = self.currency[exchange_currency_code]
            self.exchange_rate = float(self.currency_exchange['rate'])
            self.exchange_amount = round(self.exchange_rate * currency_ammount, 2)

            print(f"You received {self.exchange_amount} {exchange_currency_code.upper()}")

exchange_curr = ExchangeCurrency()

while statement:
    exchange_currency_code = input().lower()
    if exchange_currency_code == "":
        break
    currency_ammount = float(input())
    exchange_curr.currency_cache()

