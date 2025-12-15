from geopy import Nominatim

geolocator = Nominatim(user_agent="geo_app")

location = geolocator.reverse("23.2550652, 77.4255480")
print(location.address)
