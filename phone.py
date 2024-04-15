import phonenumbers
import pyfiglet
import opencage
import folium
import subprocess
text =pyfiglet.figlet_format("Phone   number   tracker ")
print(text)
number =input("Enter the Number")

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print("Name of country : ",location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print("Service Provider : " , carrier.name_for_number(service_pro ,"en"))

from opencage.geocoder import OpenCageGeocode

key = 'f8a3171a9aec4d918143a9d76a696e87'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(result)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat ,lng ],zoom_start=40)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("Mylocation.html")
