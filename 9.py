import requests, re, hashlib

url = "http://ctfq.sweetduet.info:10080/~q9/flag.html"

r = re.compile("nonce=\"([^\"]*)\"")
nonce =  r.search(requests.get(url).headers['WWW-Authenticate']).group(1)
print nonce

hash1 = "c627e19450db746b739f41b64097d449"
m = hashlib.md5()
m.update("GET:/~q9/flag.html")
hash2 = m.hexdigest()
cnonce = "9691c249745d94fc"
nc = "00000001"
qop = "auth"

n = hashlib.md5()
n.update( hash1 + ":" + nonce + ":" + nc + ":" + cnonce + ":" + qop + ":" + hash2)
res = n.hexdigest()
print res

headers = {                   # Set the appropriate headers for the response
    'Host': "ctfq.sweetduet.info:10080",
    'User-Agent': 'Mozilla',
    'Connection': 'keep-alive',
    'Authorization': 'Digest username="q9", realm="secret", nonce="' + nonce +'", uri="/~q9/flag.html", algorithm=MD5, response="' + res + '", qop=' + qop +', nc=' + nc + ', cnonce="' + cnonce + '"'
    }
r = requests.get(url,headers=headers)
print r.text
