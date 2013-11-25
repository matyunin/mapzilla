from proxies.hidemyass import MzProxyHidemyass
import pprint

def grab2():
    print 'Obtaining HideMyAss.com proxy list'

    proxy = MzProxyHidemyass()
    proxies = proxy.list()
    pprint.pprint(proxies)