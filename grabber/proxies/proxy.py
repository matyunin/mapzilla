import requests
import json
import os


class MzProxy(object):

    html = ''
    config = {}
    common_config = {}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) \
        AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'
    }

    def __init__(self, url, **kwargs):
        self.prepare_config()

        if not kwargs.get('quiet', True):
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

    def get_json_path(self):
        basedir = os.path.abspath(__file__ + '/../../..')

        return basedir + '/' + self.config['dump']['json']['file']

    def prepare_config(self):
        config_file = open('%s/config.json' % os.path.abspath(__file__ + '/../'))

        self.common_config = json.load(config_file)
        self.config = self.common_config['proxy'][self.__class__.__name__]

        config_file.close()

    def list(self):
        return json.load(open(self.get_json_path()))

    def save_json(self):
        with open(self.get_json_path(), 'w') as outfile:
            json.dump(
                self.proxies,
                outfile,
                sort_keys=True,
                indent=4,
                separators=(',', ': ')
            )