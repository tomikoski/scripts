import argparse
from urllib.parse import urlparse

def parseUrl(uu):
 u = urlparse(uu)
 print("\nscheme:\t{0}\nhost:\t{1}\npath:\t{2}\nparams:\t{3}\query:\t{4}\nfrag:\t{5}".format(u.scheme,u.hostname,u.path,u.params,u.query,u.fragment))

parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', help='url or urls',nargs='+')
args = parser.parse_args()

for a in args.url:
  parseUrl(a)
