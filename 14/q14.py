f = open('q14res.txt','r')
d = f.read();
f.close();
lines = d.split('\n')
s = ''
for line in lines:
    s += line[0:1]

print s
