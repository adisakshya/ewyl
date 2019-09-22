import sys
import json

class vehical_tracking_system :

    def __init__(self):

        f = open('bus_data.json')
        self.bus_info = json.load(f)
        f.close()
    
    def __str__(self):

        return 'vehical_tracking_system'
    
    def bus_lookup(self, bus_number):

        if bus_number not in self.bus_info.keys():
            
            print("Invalid Bus Number")
            return False
        
        bus_details = self.bus_info[bus_number]
        latitude, longitude, place, speed = bus_details['lat'], bus_details['lng'], bus_details['place'], bus_details['speed']
        is_moving = False
        
        if speed:
            is_moving = True
        
        print("Geo Location: {}, {}\nPlace: {},\nSpeed: {},\nIs Moving: {}".format(latitude, longitude, place, speed, is_moving))
        return True

def usage():

    print("USAGE: python3 cli.py <bus_number>")

if __name__ == "__main__":
    
    try:

        bus_number = sys.argv[1]
        vts = vehical_tracking_system()
        flag = vts.bus_lookup(bus_number)
        if flag:
            print("Success")
        else:
            print("No Success")

    except:

        usage()