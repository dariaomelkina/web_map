import folium
import pandas
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def read_file():
    """

    """
    data = pandas.read_csv("locations.csv", error_bad_lines=False)
    movie = data['movie']
    year = data['year']
    location = data['location']
    x = []
    for i in zip(movie, year, location):
        x.append(i)
    return x


def year_list_with_coordinates(lst, year):
    """

    """
    answer_movie = []
    answer_countries = []
    geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout=3)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    for i in lst:
        if i[1] == year:
            # location_geo = geolocator.geocode(i[2])
            # try:
            #     latitude_geo, longitude_geo = location_geo.latitude, location_geo.longitude
            # except:
            #     continue
            answer_movie.append([i])
            answer_countries.append([i[2]])
    return answer_countries, answer_countries

lst1 = read_file()
print(year_list_with_coordinates(lst1, '2000'))


def map_func(year, lat, long):
    """

    """
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    map = folium.Map(location=[lat, long], zoom_start=7, tiles='Stamen Terrain')
    zip_file = read_file()
    fg_movies = folium.FeatureGroup(name="Movies")
    for i in zip_file:
        if i[1] == year:
            location_geo = geolocator.geocode(i[2])
            latitude_geo, longitude_geo = location_geo.latitude, location_geo.longitude
            fg_movies.add_child(folium.CircleMarker(location=[latitude_geo, longitude_geo],
                                                    radius=10,
                                                    popup=i[0],
                                                    fill_color='red',
                                                    color='red', fill_opacity=0.5))
    map.add_child(fg_movies)
    map.add_child(folium.LayerControl())
    map.save('Map_2.html')

# map_func(2016, 51.509865, -0.118092)




# data = pandas.read_csv("Stan_1900.csv")
# lat = data['lat']
# lon = data['lon']
# churches = data['церкви']
# hc = data['гр-кат.']
#
# def color_creator(population):
#     if population < 2000:
#         return "green"
#     elif 2000 <= population <= 3500:
#         return "yellow"
#     else:
#         return "red"
#
#
# map = folium.Map(location=[48.314775, 25.082925],
# zoom_start=10)
# fg_hc = folium.FeatureGroup(name="Greek Catholic")
# for lt, ln, ch, hc in zip(lat, lon, churches, hc):
#   fg_hc.add_child(folium.CircleMarker(location=[lt, ln],
#                                       radius=10,
#                                       popup="1900 рік"+"\n" + ch,
#                                       fill_color=color_creator(hc),
#                                       color='red', fill_opacity=0.5))
# fg_pp = folium.FeatureGroup(name="Population")
# fg_pp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
#                                style_function=lambda x: {'fillColor':'green'
#                                if x['properties']['POP2005'] < 10000000
#                                else 'orange'if 10000000 <= x['properties']['POP2005'] < 20000000
#                                else 'red'}))
# map.add_child(fg_hc)
# map.add_child(fg_pp)
# map.add_child(folium.LayerControl())
# map.save('Map_7.html')


# if __name__ == "__main__":
#     year = input("Please enter a year you would like to have a map for: ")
#     lat, long = map((lambda x: float(x)), input("Please enter your location (format: lat, long): ").split(", "))
#     print("Map is generating...\nPlease wait...")
#     answer = 0
#     print("Finished. Please have look on the map ", answer)
