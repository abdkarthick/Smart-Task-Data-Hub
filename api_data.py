import requests


city=input("Enter city name: ")


url=f"https://wttr.in/{city}?format=j1"


try:

    result=requests.get(url)


    data=result.json()


    temp=data["current_condition"][0]["temp_C"]

    weather=data["current_condition"][0]["weatherDesc"][0]["value"]


    print("City:",city)
    print("Temperature:",temp,"C")
    print("Condition:",weather)



except:

    print("Unable to fetch data")