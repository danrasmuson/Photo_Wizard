# for the full tutorial visit this site
# http://flask.pocoo.org/docs/quickstart
from flask import Flask, url_for, request, jsonify
from imageSearch import getImageForTerm
app = Flask(__name__)

@app.route('/GetImage', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json(force=True) 
        return getImageForTerm(data['query'])
    else:
        # sent a GET
        return "500"


if __name__ == '__main__':
    app.run(debug=True)