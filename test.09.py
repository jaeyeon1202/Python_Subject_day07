# 홀수합
s=0
for i in range(1,101,2):
    s += i
print("홀수합:",s)
print("")

s=0
for i in range(1,101):
    if i%2==1:
        s += i
print("홀수합:",s)
print("")

s=0
for i in range(1,101):
    if i%2==0:
        continue
    s += i
print("홀수합:",s)
print("")

s=0
i=1
while i <=100:
    if i %2==1:
        s += i
    i += 1
print("홀수합:",s)
print("")

#리스트이용
a=[]
s=0
for i in range(1,101):
    if i % 2 ==1:
        a.append(i)

for i in a:
    s += i
print("홀수합:",s)

#리스트 표현식
a=[i for i in range(1,101,2)]
print(a)
s=0
for i in a:
    s+=i
print("홀수합:",s)

b=list(range(1,101,2))
print(b)



    
s
