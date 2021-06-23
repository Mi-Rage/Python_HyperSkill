import requests

url_path = input()
r = requests.get(url_path)
status = r.status_code
if status == 200:
    content = requests.get(url_path).content
    with open('source.html', 'wb') as file:
        file.write(content)
    print("Content saved.")
else:
    print("The URL returned ", status)
