d = {'p': 20,'q':10,'r':15}
d1 = {'p':40,'q':20,'r':5}

d2={}

for key in d:
    d2[key]=d[key]+d1[key]

print(d2)    
