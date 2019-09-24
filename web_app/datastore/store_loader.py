import json

def load_store():

    try:
        
        f = open('./datastore/store/bus_data.json', 'r')
        bus_info = json.load(f)
        f.close()
        return bus_info
    
    except Exception as error:

        print("Error:", error)
        return False

def create_store(mapping):

    try:

        f = open('./store/bus_data.json', 'w')
        json.dump(mapping, f)
        f.close()
        return True

    except Exception as error:

        print("Error:", error)
        return False

def store_api_response(json_file):

    try:

        f = open('./store/data.json', 'w')
        json.dump(json_file, f)
        f.close()
        return True

    except Exception as error:

        print("Error:", error)
        return False

def load_api_response():

    try:
        
        f = open('./store/data.json', 'r')
        res = json.load(f)
        f.close()
        return res
    
    except Exception as error:

        print("Error:", error)
        return False