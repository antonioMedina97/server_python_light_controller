import json
import re
import requests

from flask import Flask, jsonify, render_template, request, Response


def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/', methods=['GET'])
def index():
    return render_template('/index.html')


@app.route('/lights', methods=['GET', 'POST'])
def post_lights():
    if request.method == 'GET':
        return jsonify(success=False)

    # Assumes the request is going to fail
    response = jsonify(success=False)

    if request.method == 'POST':

        # Loads the json object as array
        new_color = json.loads(json.dumps(request.get_json()))

        # Test if it is an HEX color expression
        regex_test = re.search('^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$', new_color['color'])

        # If it is a valid color expression
        if not regex_test == '':
            # TODO: send a request to the raspberry to change the color

            response_from_raspberry = send_request_raspberry(new_color['color'])

            print('response from server: {}'.format(response_from_raspberry.text))

            resp_json = response_from_raspberry.json()

            print(resp_json)

            response = jsonify(success=True)
        else:
            response = jsonify(success=False)

    return response


@app.route('/sunlight', methods=['GET'])
def sunlight():
    # TODO: send a request to the raspberry to get the sunlight data
    pass


def send_request_raspberry(new_color):
    url = 'http://192.168.1.81/manage_lights'

    response_from_raspberry = requests.post(url, json={'color': new_color})

    return response_from_raspberry


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run('0.0.0.0', 80, debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
