import folium
#  Bangladesh Location
latitude = 24.098379
longitude = 90.328712
latitude1 = 24.098300
longitude1 = 90.328700
# Custom Icon
custom_icon = folium.features.CustomIcon('icon.png', icon_size=(20, 20))
#  Map
map = folium.Map(location=[latitude, longitude], zoom_start=6)
#  Marker
folium.Marker(
    [latitude, longitude], popup="Bangladesh", icon=folium.Icon(color="red", icon="home"), tooltip="My Home"
).add_to(map)
folium.Marker(
    [latitude1, longitude1], popup="Bangladesh", icon=custom_icon, tooltip="My Home"
).add_to(map)
#  Save
map.save("map.html")