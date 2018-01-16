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
CLIENT_ACCESS_TOKEN = ''
# # Page Access Token for Facebook Page where the conversation can be started with the bot.
# PAGE_ACCESS_TOKEN = 'INSERT_FACEBOOK_PAT'
# # Token created whilst configuring Webhook subscription.
# VERIFY_TOKEN = 'INSERT_TOKEN'

# An endpoint to ApiAi, an object used for making requests to a particular agent.
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
request_manager = RequestManager()


def format_response(text):
    response = '{"speech": "'+text+'"}'
    return Response(response=response,
                    status=200,
                    mimetype="application/json")


@app.route('/', methods=['GET'])
def print_signage():
    response = format_response('Yeah biatch')
    return response


@app.route('/', methods=['POST'])
def print_signage_2():
    data = request.data
    rsp = request_manager.new_request(data)
    return rsp


if __name__ == '__main__':
app.run(debug=True)