# put your python code here
duration = int(input())
foodByDayCost = int(input())
oneWayCost = int(input())
hotelNightCost = int(input())
total = foodByDayCost * duration + oneWayCost * 2 + hotelNightCost * (duration -1)
print(total)