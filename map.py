import folium

map=folium.Map(location=[28.7041, 77.1025])
fg1=folium.FeatureGroup(name="MapofDelhi")
for coordinates,info in zip([[28.7163, 77.1563],[28.6990, 77.1387],[28.6910, 77.1765],[28.7383, 77.0822],[28.6707, 77.1285],[28.7095, 77.1888],[28.6304, 77.2177]],['Shalimar Bagh','Pitampura','Ashok Vihar','Rohini','Punjabi Bagh','Model Town','CP']):
    fg1.add_child(folium.CircleMarker(location=coordinates,popup=info,icon=folium.Icon(color='green'),fill=True,fill_color='blue'))
    
fg2=folium.FeatureGroup(name="Populations")
fg2.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange'if 1000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())


map.save("Map1.html")
