import requests


class MzProxy(object):

    html = ''

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) \
        AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'
    }

    def __init__(self, url):
        self.url = url

        self.req = requests.post(
            self.url,
            data=self.data,
            cookies=self.cookies,
            headers=self.headers,
            allow_redirects=True
        )

        self.url = self.req.url
        self.html = self.req.text