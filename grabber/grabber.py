from proxies.hidemyass import MzProxyHidemyass

def grab2():
    proxy = MzProxyHidemyass()
    proxy.refresh_url()

    return

def grab():
    url = 'http://www.benzin-price.ru/'

    proxies = {
        #'http': 'http://www.someproxy.com:3128'
    }

    url_handler = urllib.urlopen(url, proxies=proxies)

    page = html.fromstring(url_handler.read())

    for link in page.xpath("//a"):
        print "Name", link.text, "URL", link.get("href")