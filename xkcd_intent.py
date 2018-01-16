from xkcd.xkcdReq import XkcdReq


class Xkcd:
    def __init__(self):
        self.XkcdReq = XkcdReq()

    def manage(self, msg):
        # Case the variable number was defined
        if msg.get_parameter('number'):
            number = msg.get_parameter('number')
            ret = self.XkcdReq.get_post(number)

        # Case the variable random was defined
        elif msg.get_parameter('random'):
            ret = self.XkcdReq.get_random()

        # Case no variable defined => return last post
        else:
            ret = self.XkcdReq.get_last_post()
        return ret
