import json
from random import randint

from utils.query import Query


class XkcdReq:
    def __init__(self):
        pass

    API_URL = "https://xkcd.com/"
    SUFFIX = "info.0.json"

    def getPost(self, i, rand=False):
        url = self.API_URL + "/" + i + "/" + self.SUFFIX
        data = Query.make_json_request(url)
        buttons = {'next': "xkcd " + str(int(i) + 1)}
        if rand:
            buttons['random'] = 'xkcd random'
        buttons['previous'] = "xkcd " + str(int(i) - 1)

        query = Query.send_card(
            data['title'],
            data['alt'],
            data['img'],
            buttons
            )
        return query

    def getRandom(self):
        data = self.queryLastPost()
        id = data['num']
        post_id = randint(1, id)
        data = self.getPost(str(post_id), True)
        return data

    def getLastPost(self):
        data = self.queryLastPost()
        buttons = {'random': "xkcd random"}
        buttons['previous'] = "xkcd "+ str(data['num'] -1)
        query = Query.send_card(
            data['title'],
            data['alt'],
            data['img'],
            buttons)
        return query

    def queryLastPost(self):
        url = self.API_URL + self.SUFFIX
        data = Query.make_json_request(url)
        return data