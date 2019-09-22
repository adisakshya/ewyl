import click
import sys
import json

__author__ = "Adisakshya Chauhan"

@click.command()
@click.argument('bus_number')
def lookup(bus_number):
    """
    This return a particular bus from the datastore

    Arguments:

        bus_number: {integer}
    """
    f = open("../bus_data.json")
    bus_info = json.load(f)
    f.close()

    if bus_number not in bus_info.keys():
            
        click.echo("Invalid Bus Number")
        return False
        
    bus_details = bus_info[bus_number]
    latitude, longitude, place, speed = bus_details['lat'], bus_details['lng'], bus_details['place'], bus_details['speed']
    is_moving = False
        
    if speed:
        is_moving = True
        
    click.echo("Geo Location: {}, {}\nPlace: {},\nSpeed: {},\nIs Moving: {}".format(latitude, longitude, place, speed, is_moving))
    return True

if __name__ == "__main__":
    lookup()