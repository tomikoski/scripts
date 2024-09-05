import hashlib
import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-H", "--hash", help="hash to test")
parser.add_argument("-P", "--password", help="password to test")

args = parser.parse_args()

if args.hash == None:
    if args.password == None:
        parser.print_help()

if args.password:
    args.hash = hashlib.sha1(args.password.encode('utf-8')).hexdigest()

if args.hash:
    firstfive = args.hash[0:5]
    lastones = args.hash[5:]

    try:
        r = requests.get("https://api.pwnedpasswords.com/range/" + firstfive)
        if r.status_code != 200:
            print("Something went so wrong since missing 200, mmmkay?")
        else:

            ihasit = 0
            for oneline in r.text.split('\n'):
                if oneline.split(':')[0].upper() == lastones.upper():
                    print("Found it (remaining hash:number of times leaked)")
                    print(oneline)
                    ihasit = 1
                    break

            if not ihasit:
                print("Yay, hash NOT found!")

    except Exception:
        print("Error while doing the magic, exit.")


