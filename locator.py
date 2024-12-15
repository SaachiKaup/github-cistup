from geopy.geocoders import Nominatim

LOCATOR = Nominatim(user_agent = "myapp")

def lat_lng_from_address(address: str) -> [float, float]:
    location = LOCATOR.geocode(address)
    if not location:
        return (None, None)
    return (location.latitude, location.longitude)

