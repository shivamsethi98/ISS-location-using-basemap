import requests
import json
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
temp = requests.get('http://api.open-notify.org/astros.json').text
y = json.loads(temp)
lidct = y["people"]
print("The number of People in the ISS are : " + str(y["number"]))
print('The People currently in ISS are' )
for person in lidct:
        print('name: ' + person['name'])

fetch = requests.get('http://api.open-notify.org/iss-now.json').text
y = json.loads(fetch)
pos = y["iss_position"]
lat = float(pos['latitude'])
longi = float(pos['longitude']) 

m = Basemap(projection='mill',resolution='l')
xpt, ypt = m(longi , lat)
m.plot(xpt, ypt, 'r^', markersize=12,label = 'ISS')
m.drawcoastlines()
m.drawcountries()
m.etopo()

plt.legend(loc=4)	
plt.show()
