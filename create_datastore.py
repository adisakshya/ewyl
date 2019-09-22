import reverse_geocoder as rg 
import json

class reverse_geo_coder:

    def __str__(self):

        return "reverse_geo_coder"

    def reverseGeocode(self, coordinates): 
        result = rg.search(coordinates) 
        
        # result is a list containing ordered dictionary. 
        result = list(result[0].items())
        name = result[2][1]
        admin1 = result[3][1]
        admin2 = result[4][1]
        cc = result[5][1]

        print(name, admin1, admin2, cc)
        return name, admin1 + ' ' + admin2, cc

class bus_info:

    def __init__(self):

        self.map = dict()

    def __str__(self):

        return "bus_info"

    def update_datastore(self):

        f = open('./data.json')
        response = json.load(f)
        f.close()

        bus_list = response['busDetails']
        for bus in bus_list:
            bus_number = bus['busNum']
            bus_reg_number = bus['busRegNum']
            route_number = bus['routeNum']
            gps = bus['gps']
            latitude = bus['lat']
            longitude = bus['lng']

            if latitude and longitude:

                rev_coder = reverse_geo_coder()
                city_name, state, country = rev_coder.reverseGeocode((latitude, longitude))

                place = city_name + ', ' + state + ', ' + country
                velocity = gps[108:]
                speed = velocity[:velocity.index(' ')]
                speed = float(speed)
                
                res = {
                    'lat': latitude,
                    'lng': longitude,
                    'place': place,
                    'speed': speed
                }

                self.map[int(bus_number)] = res

        f = open('bus_data.json', 'w')
        json.dump(self.map, f)
        f.close()

if __name__ == "__main__": 
      
    busObj = bus_info()
    busObj.update_datastore()