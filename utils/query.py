import json

import requests
from flask import Response


class Query:

    # region dialogflow
    @staticmethod
    def send_image(url):
        return '{ "imageUrl": "'+url+'", "platform": "telegram", "type": 3 }'

    @staticmethod
    def send_quick_reply(title, replies):
        ret = '{"messages": [{"platform": "telegram","replies": ['
        for v in replies:
            ret += '"'+v+'",'
        ret = ret[:-1]+'],"title": "'+title+'","type": 2}]}'
        print ret
        return ret

    @staticmethod
    def send_card(title, subtitle, img_url, buttons):
        ret = '{' \
               '"messages": ['\
               '{'\
               '"buttons": ['
        for k,v in buttons.iteritems():
            ret += '{'\
                   '"postback": "'+v+'",'\
                   '"text": "'+k+'"'\
                   '},'
        ret = ret[:-1] + '],'\
               '"imageUrl": "'+img_url+'",'\
               '"platform": "telegram",'\
               '"subtitle": "'+subtitle+'",'\
               '"title": "'+title+'",'\
               '"type": 1'\
               '}]'\
               '}'
        return ret
    # endregion

    # region request
    @staticmethod
    def make_json_request(url):
        try:
            request_response = requests.get(url)
            if request_response.status_code == 200:
                data_response = request_response.json()
                return data_response
            else:
                print " [x] Fail..."
        except requests.exceptions.RequestException as e:
            print 'Error : ' + e

    @staticmethod
    def json_to_txt(json_data):
        return json.dumps(json_data, indent=4)

    @staticmethod
    def generate_reponse(response):
        return Response(response=response,
                        status=200,
                        mimetype="application/json")
    # endregion
