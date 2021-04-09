# write your code here!
source_currency = "conicoins"
destination_currency = "dollars"
coins = int(input(f"Please, enter the number of {source_currency} you have: "))
rate = float(input("Please, enter the exchange rate: "))
exchange = coins * rate
print(f"The total amount of {destination_currency}: {exchange}")
