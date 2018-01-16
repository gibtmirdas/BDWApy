from xkcd.xkcdReq import XkcdReq


class Xkcd:
    def __init__(self):
        self.XkcdReq = XkcdReq()

    def manage(self, msg):
        if msg.get_parameter('number'):
            number = msg.get_parameter('number')
            ret = self.XkcdReq.getPost(number)
        elif msg.get_parameter('random'):
            ret = self.XkcdReq.getRandom()
        else:
            ret = self.XkcdReq.getLastPost()
        return ret

    def default(self):
        return self.XkcdReq.getPost("900")