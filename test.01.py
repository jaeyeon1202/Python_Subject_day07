# 반복문 for i in range():
#        for i in 리스트:
for i in [1,2,3,4,5]:
    print("리스트")

for i in (1,2,3,4,5):
    print("튜플")

dic={1:"a",2:"b",3:"c"}
for i in dic:
    print("딕트")

for i in {1,2,3,4,3,3,3,}:
    print("세트")

for i in "abcd":
    print("문자열")

dic={1:"a",2:"b",3:"c"}
for i in dic:
    print(i,end="")

for i in dic.values():
    print(i,end="")

for i in dic.items():
    print(i,end="")