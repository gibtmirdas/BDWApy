from utils.query import Query
from dialogFlowMessage import DialogFlowMessage


class RequestManager:

    def __init__(self):
        pass

    def new_request(self, json_txt):
        self.msg = DialogFlowMessage(json_txt)
        if self.msg.intent is not None:
            return self.msg.intent.manage(self.msg)
        return Query.generate_reponse("")
