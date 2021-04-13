# write your code here!
import requests
import json

currency = input().lower()
url = f"http://www.floatrates.com/daily/{currency}.json"
r = requests.get(url)
value = json.loads(r.text)
print(value['usd'])
print(value['eur'])

