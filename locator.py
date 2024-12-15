from geopy.geocoders import Nominatim


'''
address = input()
locator = Nominatim(user_agent = "myapp")
location = locator.geocode(address)

print(location)
'''


import geocoder

g = geocoder.google(input())
print(g)

print(g.latlng)
