from app import *
from flask_googlemaps import GoogleMaps, Map
#initialize the google maps
google_maps = GoogleMaps(app)




@app.route('/map/data', methods=['GET'])
def get_map_data():
    map_data = {
        'center': {'lat': 37.4224, 'lng': -122.0841},
        'zoom': 12
    }
    
    return jsonify(map_data)


