import what3words
import os
from flask import Flask, request, url_for, redirect, abort

api_key = os.environ.get("API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():

    if len(request.args) == 1:
        location_words = request.args["words"]
        location_check = location_words.split(".")
        if len(location_check) == 3:
            return redirect(url_for("words_to_coordinates", words=location_words))

    abort(400)

@app.route("/words_to_coordinates")
def words_to_coordinates():

    if len(request.args) == 1:
        location_3_words = request.args["words"]

        # API Key addded in API call variable.
        geocoder = what3words.Geocoder(api_key)

        contents = geocoder.convert_to_coordinates(location_3_words)

        if "error" in contents:
            abort(400)

        return contents
    
    abort(400)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
