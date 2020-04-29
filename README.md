# Scripts
Scripts and stuff! So much, so little, we haz it all!

## hibp.py
Inspired by several projects from NPM world, I wrote my own in python.
Idea is that one can safely check their password from https://haveibeenpwned.com/ site using simple python script. Either you can use hash of your password or the actual password and this script will check how many times it has been leaked. Only first 5 characters of a SHA-1 password hash are being sent to HIBP API.

* Example usage
```
# using password
python3 hibp.py -P Qwerty123!
Found it (remaining hash:number of times leaked)
DEC8C7BC9675182779E564FAE1327D30F9B:347

# using SHA-1 hash
python hibp.py -H d4f55dec8c7bc9675182779e564fae1327d30f9b
Found it (remaining hash:number of times leaked)
DEC8C7BC9675182779E564FAE1327D30F9B:347

# Final test with my personal password which hasn't yet leaked...
python hibp.py -P PerkeleenPerunat666
Yay, hash NOT found!
```

* Requirements
```
pip install requests
```

## urlparser.py
Parse URLs (scheme, host, ...)

* Example usage
```
python urlparser.py -u "https://duckduckgo.com/?q=github&t=h_&ia=web" \
"https://www.google.com/search?q=duckduckgo&oq=duck&aqs=chrome...&sourceid=chrome&ie=UTF-8"

scheme:	https
netloc:	duckduckgo.com
host:	duckduckgo.com
path:	/
params:	\query:	q=github&t=h_&ia=web
frag:	

scheme:	https
netloc:	www.google.com
host:	www.google.com
path:	/search
params:	\query:	q=duckduckgo&oq=duck&aqs=chrome...&sourceid=chrome&ie=UTF-8
frag:	
```
