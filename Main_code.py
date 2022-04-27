import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.gismeteo.ru/weather-michurinsk-4438/2-weeks/"



headers = {

    "Accept": "*/*",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

req = requests.get(url, headers= headers)
src = req.text

# with open('index.html',encoding='utf-8') as file:
#     src = file.read()

soup = BeautifulSoup(src, 'lxml')


all_days = soup.find_all(class_='day')
all_dates = soup.find_all(class_='date')
max_temp = soup.find_all(class_='maxt')
min_temp = soup.find_all(class_='mint')
conditions_raw = soup.find_all(class_='weather-icon tooltip')
wind_units = soup.find_all(class_='wind-unit unit unit_wind_m_s')
precipitations = soup.find(class_='widget-row widget-row-precipitation-bars row-with-caption').find_all(class_='row-item')


precips = []

for item in precipitations:
    precips.append(item.text)

wind=[]


for c in wind_units:
    wind.append(c.getText())



conditions=[]
for c in conditions_raw:
    conditions.append(c.get('data-text'))

maxt = []
for c in max_temp[:14]:
    maxt.append(c.find(class_='unit unit_temperature_c').text)

mint = []
for c in min_temp[:14]:
    mint.append(c.find(class_='unit unit_temperature_c').text)




all_dates = all_dates[:14]
all_days = all_days[:14]
max_temp = max_temp[:14]

for i in range(14):
    print (f'{all_days[i].text} {all_dates[i].text} t max = {maxt[i]} t min = {mint[i]} {conditions[i]} , ветер {wind[i]} м/c , осадки {precips[i]} мм')




