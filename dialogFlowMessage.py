import json
from utils.vars import Vars


class DialogFlowMessage:

    def __init__(self, json_txt):
        print json_txt
        self.intent_name = None
        self.intent = None
        self.js = None
        self.parse_json(json_txt)
        self.get_intent()

    def get_intent(self):
        self.intent_name = self.js['result']['metadata']['intentName']
        self.intent = Vars.INTENT[self.intent_name]

    def parse_json(self, json_txt):
        self.js = json.loads(json_txt)

    def get_parameter(self, name):
        print name
        p = None
        if len(self.js['result']['parameters']) != 0:
            print self.js['result']['parameters']
            p = self.js['result']['parameters'][""+name]
        if p == "":
            return None
        return p
