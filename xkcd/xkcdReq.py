import json
from random import randint

from utils.query import Query


class XkcdReq:
    def __init__(self):
        pass

    API_URL = "https://xkcd.com/"
    SUFFIX = "info.0.json"

    def get_post(self, i, rand=False):
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

    def get_random(self):
        data = self.query_last_post()
        id = data['num']
        post_id = randint(1, id)
        data = self.get_post(str(post_id), True)
        return data

    def get_last_post(self):
        data = self.query_last_post()
        buttons = {'random': "xkcd random"}
        buttons['previous'] = "xkcd "+ str(data['num'] -1)
        query = Query.send_card(
            data['title'],
            data['alt'],
            data['img'],
            buttons)
        return query

    def query_last_post(self):
        url = self.API_URL + self.SUFFIX
        data = Query.make_json_request(url)
        return data
