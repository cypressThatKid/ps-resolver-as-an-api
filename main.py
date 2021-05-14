import requests, sys, re

username = sys.argv[1]

r = requests.get('https://playstationresolver.xyz/profile/{}'.format(username))

grabbed = re.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})', r.text)

for x in grabbed:
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', x):
                print("{} resolves to: {}".format(username, x))
