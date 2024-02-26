import requests

# Установить URL-адрес и параметры запроса (в данном случае, город и ваш API-ключ)
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Truskavets",
    "appid": "5f60aef3a1c51552b68517c15890f00a",  # Замените "YOUR_API_KEY" на ваш ключ API
}

# Выполнить запрос
response = requests.get(url, params=params)

# Проверить статус ответа
if response.status_code == 200:
    # Распарсить JSON-ответ
    data = response.json()
    # Вывести данные о погоде
    print(data)
else:
    print("Ошибка при запросе:", response.status_code)
