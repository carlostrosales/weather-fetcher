import requests
# from twilio.rest import Client


# account_sid = ''
# auth_token = ''

API_KEY = "81c5ef6524a48da83a2d248a85a9ccaa"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
# client = Client(account_sid, auth_token)

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = str(data['weather'][0]['description'])
    temperature = str(round(data["main"]["temp"] - 273.15, 2))
    message = weather + temperature
    print("Weather: ", weather)
    print("Temperature: ", temperature, "celsius")
    # message = client.messages.create(body='Test', from_='+18333668498',to='+14698379549')
    # print(message.sid)
    resp = requests.post('https://textbelt.com/text', {'phone': '4698379549', 'message': message, 'key': 'textbelt',})
    print(resp.json())
else:
    print("An error occurred.")

