# -*- coding: utf-8 -*-

import random
from proxies.hidemyass import MzProxyHidemyass

import re
import sys
import json
import signal
import requests
import chardet
import cssutils
import threading

from cssutils import css
from BeautifulSoup import BeautifulSoup


class MzGrabber(object):

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4,da;q=0.2,de;q=0.2,fr;q=0.2,ja;q=0.2,uk;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.benzin-price.ru',
        'Referer': 'http://www.benzin-price.ru/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'
    }

    def grab(self):
        self.grab_regions()

    def grab_regions(self):
        proxy = self.get_fresh_proxy()
        url = 'http://www.benzin-price.ru/zapravka.php?page=region'

        req = requests.get(
            url,
            proxies={
                '%s' % proxy['type'].lower(): '%s://%s:%s' % (proxy['type'].lower(), proxy['host'], proxy['port'])
            }
        )

        soup = BeautifulSoup(req.text, fromEncoding='windows-1251')
        print soup.text.decode('utf-8')
        print chardet.detect(soup.text)

    def get_fresh_proxy(self):
        proxy_handler = MzProxyHidemyass(quiet=True)
        proxies = proxy_handler.list()

        return random.choice(proxies)