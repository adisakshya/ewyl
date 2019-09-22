import reverse_geocoder as rg 
  
def reverseGeocode(coordinates): 
    result = rg.search(coordinates) 
      
    # result is a list containing ordered dictionary. 
    result = list(result[0].items())
    name = result[2][1]
    admin1 = result[3][1]
    admin2 = result[4][1]
    cc = result[5][1]

    print(name, admin1, admin2, cc)
    return name, admin1, admin2, cc

if __name__=="__main__": 
      
    coordinates = (36.778259, -119.417931) 
      
    reverseGeocode(coordinates)