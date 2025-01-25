import requests
import pprint

params = {
    'q': 'html'
}

response = requests.get('https://api.github.com/search/repositories', params=params)

response_json = response.json()

print(f"Количество репозиториев с использованием html: {response_json['total_count']}")
print(response.status_code)
