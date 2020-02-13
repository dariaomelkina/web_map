import pandas
from geopy.geocoders import Nominatim


def generate():
    """
    Generates new file, using locations.csv.
    Adds coordinates of the location (latitude, longitude).
    """
    geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout=3)
    data = pandas.read_csv("locations1.csv", error_bad_lines=False)
    locations = data['location']
    latitude_lst = []
    longitude_lst = []
    for i in locations:
        try:
            location_geo = geolocator.geocode(i, timeout=5)
            latitude_lst.append(location_geo.latitude)
            longitude_lst.append(location_geo.longitude)
        except AttributeError:
            latitude_lst.append('a')
            longitude_lst.append('a')
    data['latitude'] = latitude_lst
    data['longitude'] = longitude_lst
    print(data)

    
generate()
