import cssutils
from cssutils import css
import requests
from BeautifulSoup import BeautifulSoup
from proxy import MzProxy


class MzProxyHidemyass(MzProxy):

    url = 'http://hidemyass.com/proxy-list/'
    cookies = {}
    data = {}
    proxies = []

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4,da;q=0.2,de;q=0.2,fr;q=0.2,ja;q=0.2,uk;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=2et6icdkv3hvajvn3fd6g9nd60;',
        'Host': 'hidemyass.com',
        'Referer': 'http://hidemyass.com/proxy-list/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'
    }

    def __init__(self):
        super(MzProxyHidemyass, self).__init__(self.url)
        self.refresh_url()

    def list(self):
        soup = BeautifulSoup(self.html)
        table = soup.find(id='listtable')
        table.thead.decompose()

        for tr in table.findAll('tr'):
            tds = tr.findAll('td')

            address = {
                'host': self.parse_host(tds, self.parse_css(tr.find('style').string)),
                'port': self.parse_port(tds),
                'type': self.parse_type(tds),
                'speed': self.parse_speed(tds),
                'country': self.parse_country(tds)
            }

            self.proxies.append(address)

        return self.proxies

    @staticmethod
    def parse_css(css):
        style = {}

        for rule in cssutils.parseString(css):
            if rule.type == rule.STYLE_RULE:
                style[rule.selectorText.replace('.', '')] = not rule.style.display.lower() == 'none'

        return style

    @staticmethod
    def parse_host(tds, style):
        ip = []
        container = tds[1].find('span')

        container.find('style').decompose()

        for block in container:
            if type(block).__name__ == 'NavigableString':
                ip.append(block.string)
                continue

            block_style = block.get('style')
            block_class = block.get('class')

            if block_style:
                css_style = css.CSSStyleDeclaration(cssText=block_style)

                if css_style.getPropertyCSSValue('display').cssText.lower() == 'none':
                    continue

            if block_class in style and not style[block_class]:
                continue

            if block.string is None:
                continue

            ip.append(block.string)

        return ''.join(ip)

    @staticmethod
    def parse_port(tds):
        return int(tds[2].string)

    @staticmethod
    def parse_speed(tds):
        css_string = tds[4].find('div').find('div').get('style')
        css_style = css.CSSStyleDeclaration(cssText=css_string)

        return int(css_style.getPropertyCSSValue('width').cssText.strip('%'))

    @staticmethod
    def parse_type(tds):
        return tds[6].string.strip()

    @staticmethod
    def parse_country(tds):
        return tds[3].find('span').find(
            text=True,
            recursive=False
        ).strip()

    def refresh_url(self):
        print '[?]', 'Retrieving new url via \'%s\'' % self.url

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

        r = requests.post(
            self.url,
            data=data,
            headers=self.headers,
            cookies=self.cookies,
            allow_redirects=True
        )

        self.url = r.url
        self.cookies['PHPSESSID'] = r.cookies['PHPSESSID']

        print '[!]', 'Retrieved \'%s\'' % self.url