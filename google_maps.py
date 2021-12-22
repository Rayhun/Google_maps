import folium
#  Bangladesh Location
latitude = 24.098379
longitude = 90.328712
latitude1 = 24.098300
longitude1 = 90.328700
# Custom Icon
custom_icon = folium.features.CustomIcon('icon.png', icon_size=(20, 20))
#  Map
map = folium.Map(location=[latitude, longitude], zoom_start=12, control_scale=True)
#  Marker
folium.Marker(
    [latitude, longitude], popup="Bangladesh", icon=folium.Icon(color="red", icon="home"), tooltip="My Home"
).add_to(map)
folium.Marker(
    [latitude1, longitude1], popup="Bangladesh", icon=custom_icon, tooltip="My Home"
).add_to(map)

# Circle Marker
folium.CircleMarker(
    location=[latitude, longitude], radius=100, popup="Bangladesh",
    color="green", fill_color="gray", fill_opacity=0.6, tooltip="My Home",
    fill=True, stroke=True, weight=2, opacity=0.8
).add_to(map)
# add tiles to the map
map.add_child(folium.raster_layers.TileLayer(
    tiles='Stamen Terrain', attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
))
map.add_child(folium.raster_layers.TileLayer(
    tiles='Stamen Toner', attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
))
map.add_child(folium.raster_layers.TileLayer(
    tiles='Stamen Watercolor', attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
))
map.add_child(folium.raster_layers.TileLayer(
    tiles='OpenStreetMap', attr='Map tiles by OpenStreetMap, under CC BY SA.'
))
map.add_child(folium.raster_layers.TileLayer(
    tiles='CartoDB Positron', attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
))
map.add_child(folium.raster_layers.TileLayer(
    tiles='CartoDB DarkMatter', attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
))
map.add_child(folium.raster_layers.TileLayer(
    tiles='CartoDB PositronNoLabels', attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
))
map.add_child(folium.raster_layers.TileLayer(
    tiles='CartoDB PositronOnlyLabels', attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
))
map.add_child(folium.raster_layers.TileLayer(
    tiles='CartoDB DarkMatterNoLabels', attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
))
map.add_child(folium.raster_layers.TileLayer(
    tiles='CartoDB DarkMatterOnlyLabels', attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
))
folium.LayerControl().add_to(map)
#  Save
map.save("map.html")