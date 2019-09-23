from flask import Flask, render_template, request
from datastore.store_loader import load_store as store

app = Flask(__name__)
bus_data = store()

@app.route("/api/bus/<bus_number>", methods = ["GET"])
def get(bus_number):
    if request.method == "GET":

        try:

            bus_info = bus_data[bus_number]
            latitude = float(bus_info['lat'])
            longitude = float(bus_info['lng'])
            place = bus_info["place"]
            speed = bus_info['speed']

            res = {
                "success": True,
                "error": None,
                "bus_number": bus_number,
                "latitude": latitude,
                "longitude": longitude,
                "place": place,
                "speed": speed
            }

            return res

        except KeyError:

            return { "success": False, "error": "Not a valid bus number !", "response": None }
        
@app.route("/",methods = ["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)