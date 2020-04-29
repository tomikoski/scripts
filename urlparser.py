import argparse
from urllib.parse import urlparse

def parseUrl(uu):
 u = urlparse(uu)
 print("\nscheme:\t{0}\nnetloc:\t{1}\nhost:\t{2}\npath:\t{3}\nparams:\t{4}\query:\t{5}\nfrag:\t{6}".format(u.scheme,u.netloc,u.hostname,u.path,u.params,u.query,u.fragment))

parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', help='url or urls',nargs='+')
args = parser.parse_args()

for a in args.url:
  parseUrl(a)
