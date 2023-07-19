dan=int(input("단:"))
if 2<=dan<=9:
    for i in range(1,10):
        print("%d*%d=%d"%(dan,i,dan*i))
else:
    print("2~9사이 수")
    
print("")

a=[]
for i in range(1,10):
    tmp=i*2
    a.append(tmp)
print(a)
print("")

#이차원 리스트
gugu=[]
for i in range(2,10):
    tmp=[]
    for j in range(1,10):
        tmp.append(i*j)
    gugu.append(tmp)
print(gugu)