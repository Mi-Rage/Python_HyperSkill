# write your code here!
source_currency = "conicoins"
destination_currency = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}

coins = float(input())
for key in destination_currency:
    rate = round(coins * destination_currency[key], 2)
    print(f"I will get {rate} {key} from the sale of {coins} conicoins.")

