# Задание 1
import requests
import json

url = 'https://api.github.com'
user = 'schepiga'
req = requests.get(f'{url}/users/{user}/repos')
data = json.loads(req.text)
print(f" Перечень репозитеориев пользователя {user}:")
for i in req.json():
    print(i['name'])

# Задание 2
url = 'https://www.amdoren.com/api/currency.php'
api_key = 'EkekcMgKtj6VEVngjNRsBHc3pNwC6n'
cur1 = 'USD'
cur2 = 'RUB'

my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/91.0.4472.164 Safari/537.36'}

my_params = {'api_key': api_key,
             'from=': cur1,
             'to=': cur2,
             'amount=': '1'}

response = requests.get(url, params=my_params, headers=my_headers)
j_data = response.json()
print(j_data)
