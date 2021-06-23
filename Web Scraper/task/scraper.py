import requests

url_path = input()
r = requests.get(url_path)
if r.status_code == 200 and 'content' in r.json().keys():
    print(r.json()['content'])
else:
    print("Invalid quote resource!")
