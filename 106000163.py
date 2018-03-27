##10600016300

typing=input("Please type anything")
d={}
for b in typing:
    if(b in d):
        d[b]=(d[b]+1)
    else:
        d[b]=1
word=d.keys()
number=d.values()
for item in d.items():
    word,number=item
    print("'"+word+"'",":",number)

#https://blog.csdn.net/qq807237096/article/details/68940848