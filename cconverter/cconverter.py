# write your code here!
coins = int(input())
source_currency = "conicoins"
destination_currency = "dollars"
rate = 100
exchange = coins * rate
print(f"I have {coins} {source_currency}.")
print(f"{coins} {source_currency} cost {exchange} {destination_currency}.")
print("I am rich! Yippee!")
