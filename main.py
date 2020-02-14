import folium
import pandas
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout=3)
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


def check_coordinates(lat, long, location):
    """

    """
    your_lat = int(lat)
    your_long = int(long)
    cond1 = range(your_lat - 1, your_lat + 2)
    cond2 = range(your_long - 1, your_long + 2)
    print(1)
    try:
        location_geo = geolocator.geocode(location)
        latitude_geo, longitude_geo = location_geo.latitude, location_geo.longitude
        print(latitude_geo, longitude_geo)
        if int(latitude_geo) in cond1 and int(longitude_geo) in cond2:
            return True
        return False
    except:
        return False


def generate_tuple(x, year, lat, long):
    """

    """
    for i in x:
        if str(i[1]) == year:
            if check_coordinates(lat, long, i[2]):
                yield i


def read_file():
    """

    """
    data = pandas.read_csv("locations.csv", error_bad_lines=False, warn_bad_lines=False)
    movie = data['movie']
    year = data['year']
    location = data['location']
    x = []
    for i in zip(movie, year, location):
        x.append(i)
    return x


def map_func(year, lat, long):
    """
    (str, float, float) -> None
    """
    map = folium.Map(location=[lat, long], zoom_start=7, tiles='Stamen Terrain')
    fg_movies = folium.FeatureGroup(name="Movies")
    fg_connection = folium.FeatureGroup(name="Connection")
    finished_list = []
    x = read_file()
    mygenerator = generate_tuple(x, year, lat, long)
    counter = 0
    for i in mygenerator:
        finished_list.append(i)
        counter += 1
        if counter == 10:
            break
    points = []
    for i in finished_list:
        location_geo = geolocator.geocode(i[2], timeout=5)
        latitude_geo, longitude_geo = location_geo.latitude, location_geo.longitude
        points.append((latitude_geo, longitude_geo))
        fg_movies.add_child(folium.CircleMarker(location=(latitude_geo, longitude_geo),
                                                radius=10,
                                                popup=i[0],
                                                fill_color='yellow',
                                                color='blue',
                                                fill_opacity=0.6))
    fg_connection.add_child(folium.PolyLine(points, color='yellow'))
    map.add_child(fg_movies)
    map.add_child(fg_connection)
    map.add_child(folium.LayerControl())
    map.save('Map.html')


# map_func('2000', 51.5074, -0.1278)


if __name__ == "__main__":
    year = input("Please enter a year you would like to have a map for: ")
    lat, long = map((lambda x: float(x)), input("Please enter your location (format: lat, long): ").split(", "))
    print("Map is generating...\nPlease wait...")
    map_func(year, lat, long)
    print("Finished. Please have look on the map Map.html")
