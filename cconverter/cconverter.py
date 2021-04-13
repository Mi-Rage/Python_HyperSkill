import requests
import json

storage = {}
source_currency = ""


def in_storage(currency):
    print("Checking the cache...")
    if currency in storage:
        return True
    else:
        return False


def calc_storage(currency, volume):
    return round(storage[currency] * volume, 2)


def get_value(currency, volume):
    url = f"http://www.floatrates.com/daily/{source_currency}.json"
    rate = get_rate(url, currency)
    return round(rate * volume, 2)


def get_rate(url, currency):
    r = requests.get(url)
    quotes = json.loads(r.text)
    rate = quotes[currency]['rate']
    storage[currency] = rate
    return rate


def get_usd_eur_rates(currency):
    target_currency = ['usd', 'eur']
    if currency == 'usd':
        target_currency.remove('usd')
    elif currency == 'eur':
        target_currency.remove("eur")

    for c in target_currency:
        url = f"http://www.floatrates.com/daily/{currency}.json"
        get_rate(url, c)


def main():
    global source_currency
    source_currency = input().lower()
    get_usd_eur_rates(source_currency)
    while True:
        destination_currency = input().lower()
        if destination_currency == "":
            break
        volume = float(input())
        if in_storage(destination_currency):
            print("Oh! It is in the cache!")
            value = calc_storage(destination_currency, volume)
        else:
            print("Sorry, but it is not in the cache!")
            value = get_value(destination_currency, volume)
        print(f"You received {value} {destination_currency}.")


if __name__ == '__main__':
    main()
