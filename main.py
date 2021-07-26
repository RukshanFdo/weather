import requests

from datetime import datetime

apiKey = 'ee037b905c887c1b37601b8eb9f2a409'
location = input("Enter city name: ")


response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + apiKey)
data = response.json()


temp = ((data['main']['temp']) - 273.15)
dis = data['weather'][0]['description']
h = data['main']['humidity']
wind = data['wind']['speed']
date = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp))
print("Current weather desc  :", dis)
print("Current Humidity      :", h, '%')
print("Current wind speed    :", wind, 'kmph')

print("====================================================")


txtlist = [temp, dis, h, wind, date]

with open("output.txt", mode='w', encoding='utf-8') as f:

    f.write("------------------------------------------------------------- \n ")
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date))
    f.write("\n ------------------------------------------------------------- \n")
    f.write("Current temperature is: {:.2f} deg C\n".format(txtlist[0]))

    f.write("{},{} \n".format("Current weather desc  :", txtlist[1]))
    f.write("{},{},{} \n".format("Current Humidity      :", txtlist[2], "%"))
    f.write("{},{},{} \n".format("Current wind speed    :", txtlist[3], "kmph"))
    f.write("====================================================")