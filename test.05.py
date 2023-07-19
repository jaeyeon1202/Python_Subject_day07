#break /continue
for i in [1,2,3,4,5]:
    if i==4:
        break
    if i %2==0:
        print(i,end="")
print("")
print("최종i:",i)