# https://dialogflow.com/docs/reference/agent/message-objects

import json
import os
import sys
from requestManager import RequestManager

from flask import Flask, request, Response

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

app = Flask(__name__)

# Client Access Token for accessing our API AI Bot
CLIENT_ACCESS_TOKEN = 'ENTER_YOUR_API_TOKEN'
# Init apiai api
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
request_manager = RequestManager()


@app.route('/', methods=['GET'])
def route_get():
    response = '{"speech": "Yeah !"}'
    return Response(response=response,
                    status=200,
                    mimetype="application/json")


@app.route('/', methods=['POST'])
def route_post():
    data = request.data
    rsp = request_manager.new_request(data)
    return rsp


if __name__ == '__main__':
    app.run(debug=True)
