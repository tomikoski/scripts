# Scripts
Scripts and stuff! So much, so little, we haz it all!

## ip-converter.py
Super old one-liner which converts an IP into different forms (hex, integer, etc.)
* Example usage
```
$ python3 ip-converter.py 1.1.1.1

org:	1.1.1.1
dec:	16843009
bin:	00000001.00000001.00000001.00000001
oct:	0001.0001.0001.0001
hex:	0x01010101
```

## hibp.py
Inspired by several projects from NPM world, I wrote my own in python.
Idea is that one can safely check their password from https://haveibeenpwned.com/ site using simple python script. Either you can use hash of your password or the actual password and this script will check how many times it has been leaked. Only first 5 characters of a SHA-1 password hash are being sent to HIBP API.

* Example usage
```
# using password
$ python3 hibp.py -P Qwerty123!

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
$ python3 urlparser.py -u "https://duckduckgo.com/?q=github&t=h_&ia=web" 

"https://www.google.com/search?q=duckduckgo&oq=duck&aqs=chrome...&sourceid=chrome&ie=UTF-8#12345"

scheme:	https
host:	duckduckgo.com
path:	/
params:	\query:	q=github&t=h_&ia=web
frag:	

scheme:	https
host:	www.google.com
path:	/search
params:	\query:	q=duckduckgo&oq=duck&aqs=chrome...&sourceid=chrome&ie=UTF-8
frag:	12345
```

## gendatepwd.py
Generate passwords using years and months (inspired by a talk in HelSec) :)
* Example usage (1728 lines of stuff)
```
$ python3 gendatepwd.py fi_FI en_US

2017Dec
Dec2017
2017dec
dec2017
2017DEC
DEC2017
2017December
December2017
2017december
december2017
2017DECEMBER
DECEMBER2017
...
...
2020Tam
Tam2020
2020tam
tam2020
2020TAM
TAM2020
2020Tammikuu
Tammikuu2020
2020tammikuu
tammikuu2020
2020TAMMIKUU
TAMMIKUU2020
```


* Example usage 1990 - to current year 2022 (14256 lines of stuff)
```
$ python gendatepwd.py -s 1990 fi_FI en_US

1990Tam
Tam1990
1990tam
tam1990
1990TAM
TAM1990
1990Tammikuu
Tammikuu1990
1990tammikuu
tammikuu1990
1990TAMMIKUU
TAMMIKUU1990
1990Hel
Hel1990
1990hel
hel1990
1990HEL
HEL1990
...
...
October2022
2022october
october2022
2022OCTOBER
OCTOBER2022
2022Nov
Nov2022
2022nov
nov2022
2022NOV
NOV2022
2022November
November2022
2022november
november2022
2022NOVEMBER
NOVEMBER2022
2022Dec
Dec2022
2022dec
dec2022
2022DEC
DEC2022
2022December
December2022
2022december
december2022
2022DECEMBER
DECEMBER2022
```
