s=0
for i in [1,2,3,4,5]:
    s += i
print("s:",s)

s=0
for i in "230319":
    s += int(i)
print(s)

s=0
for i in [2,3,0,3,1,9]:
    s += i
print(s)

s=0
a=[]
h=int(input("학번:"))
for i in a:
    a.append(h)
    s += [i]
print("학번:%d, 합:%d" % (h,s))