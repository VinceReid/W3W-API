import what3words
import os
from flask import Flask, request, url_for, redirect, abort, jsonify

api_key = os.environ.get("API_KEY")

app = Flask(__name__)

@app.route("/")
def index():

    return "Check out Tangiblink.io for info on this API"

@app.route("/words_check", methods=["GET"])
def words_check():

    if len(request.args) == 1:
        if "words" in request.args:
            location_words = request.args["words"]
            location_check = location_words.split(".")
            for word in location_check:
                if len(word) == 0:
                    return jsonify(result=3)
            if len(location_check) == 3:
                # API Key addded in API call variable.
                geocoder = what3words.Geocoder(api_key)

                contents = geocoder.convert_to_coordinates(location_words)

                if "error" in contents:
                    return jsonify(result=2)

                elif location_words == contents["words"]:
                    return jsonify(result=1)
                
                else:
                    return jsonify(result=6)
            
            if len(location_check) != 3:
                return jsonify(result=3)
        else:
            return jsonify(result=5)
        
    elif len(request.args) != 1:
        return jsonify(result=4)
    
    return jsonify(result=6)

# words check results:
#  result: 1 = "words address is correct"
#  result: 2 = "words address does not exist"
#  result: 3 = "incorrect number of words provided"
#  result: 4 = "incorrect number of arguments provided. Words to be provided as a single string seperated by punctuation mark '.' e.g. "prom.cape.pump:".
#  result: 5 = "incorrect argument type provided"
#  result: 6 = "some other fatal error"

# Coordinates to Words - Return Words

# Bulk coordinates to words

# Words - Get surrounding Square words (CENTER, N, NE, E, SE, S, SW, W, NW)

# Square size in micrometers width x height

# Haversine - Distance between 2 points

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
