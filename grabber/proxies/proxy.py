import urllib
from lxml import html
import pprint


class MzProxy(object):

    def __init__(self, url):
        self.url = url
        self.tree = html.fromstring(urllib.urlopen(self.url).read())

    def get_links(self):

        for tr in self.tree.xpath("//table[@id='listtable']//tr"):
            for td in tr.xpath("//td"):
                print td, ']' + '-' * 30
                print html.tostring(td, pretty_print=True)