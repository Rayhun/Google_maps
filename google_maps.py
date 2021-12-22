import folium
#  Bangladesh Location
latitude = 23.8103
longitude = 90.4125
#  Map
map = folium.Map(location=[latitude, longitude], zoom_start=6)
#  Marker
folium.Marker([latitude, longitude], popup="Bangladesh").add_to(map)
#  Save
map.save("map.html")
# map = folium.Map(location=[45.5236, -122.6750], zoom_start=12)
# map.save('map.html')