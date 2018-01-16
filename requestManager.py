from utils.query import Query
from dialogFlowMessage import DialogFlowMessage
from dickpic_intent import Dickpic


class RequestManager:

    def __init__(self):
        pass

    def new_request(self, json_txt):
        self.msg = DialogFlowMessage(json_txt)
        rsp = None
        if self.msg.intent is not None:
            return self.msg.intent.manage(self.msg)
        return Query.generate_reponse("")

    def dickpic(self, intent):
        """
        :type intent: Dickpic
        """
        img_url = intent.default()
        attachments = dict()
        attachments['attachments'] = dict()
        attachments['attachments']['payload'] = dict()
        attachments['attachments']['payload']['elements'] = dict()
        attachments['attachments']['payload']['elements']['image_url'] = img_url
        return attachments