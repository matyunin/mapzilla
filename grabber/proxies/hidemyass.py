import urllib
import urllib2
from proxy import MzProxy


class MzProxyHidemyassRedirectHandler(urllib2.HTTPRedirectHandler):


class MzProxyHidemyass(MzProxy):

    url = 'http://hidemyass.com/proxy-list/search-226716/'

    def http_error_302(self, req, fp, code, msg, headers):
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)

    http_error_301 = http_error_303 = http_error_307 = http_error_302

    def __init__(self):
        super(MzProxyHidemyass, self).__init__(self.url)

    def refresh_url(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'
        }

        data = {
            'ac': 'on',
            'c[]': [
                'China',
                'Indonesia',
                'Venezuela',
                'Brazil',
                'Thailand',
                'Poland',
                'Russian Federation',
                'United States',
                'Colombia',
                'Ukraine',
                'Bulgaria',
                'Iran',
                'India',
                'United Kingdom',
                'Egypt',
                'Korea, Republic of',
                'Nigeria',
                'Argentina',
                'Kenya',
                'Serbia',
                'Germany',
                'Czech Republic',
                'Cambodia',
                'Ecuador',
                'Iraq',
                'Latvia',
                'Taiwan',
                'Netherlands',
                'Slovakia',
                'Chile',
                'Taiwan',
                'Greece',
                'Japan',
                'Austria',
                'Ghana',
                'Honduras',
                'Australia',
                'Romania',
                'Peru',
                'Moldova, Republic of',
                'Pakistan',
                'Mexico',
                'Antigua and Barbuda',
                'Viet Nam',
                'France',
                'Estonia',
                'Kyrgyzstan',
                'Switzerland',
                'Bosnia and Herzegovina',
                'Palestinian Territory, Occupied',
                'Jamaica',
                'Bolivia',
                'Saudi Arabia',
                'Canada',
                'Turkey',
                'Hong Kong',
                'Italy',
                'Bangladesh',
                'United Arab Emirates',
                'Singapore',
                'South Africa',
                'Kazakhstan',
                'Sweden',
                'Croatia',
                'Tanzania, United Republic of'
            ],
            'p': '',
            'pr[]': '0',
            'a[]': ['0', '1', '2', '3', '4'],
            'sp[]': '3',
            'ct[]': '3',
            's': '1',
            'o': '0',
            'pp': '3',
            'sortBy': 'response_time'
        }

        data = urllib.urlencode(data)

        opener = urllib2.build_opener(MzProxyHidemyassRedirectHandler)
        urllib2.install_opener(opener)

        req = urllib2.Request(self.url, data, headers)
        response = urllib2.urlopen(req)

        print response.geturl()