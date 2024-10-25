import math

EARTH_RADIUS = 6371.01

latitude_1 = math.radians(float(input("Enter latitude coordinate 1: ")))
longitude_1 = math.radians(float(input("Enter longitude coordinate 1: ")))
latitude_2 = math.radians(float(input("Enter latitude coordinate 2: ")))
longitude_2 = math.radians(float(input("Enter longitude  coordinate 2: ")))

dlongitude = longitude_2 - longitude_1
dlatitude = latitude_2 - latitude_1
a = math.sin(dlatitude/2)*2 + math.cos(latitude_1) * math.cos(latitude_2) * math.sin(dlongitude/2)*2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
distance = EARTH_RADIUS * c
print(f"Distance between points is: {distance:.2f} km")