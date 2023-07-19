list_a=[]
for i in ["A반","B반","C반"]:
    tmplist=[]
    for j in ["국어","영어","수학"]:
        tmp=int(input(i+j+"점수입력:"))
        tmplist.append(tmp)
    list_a.append(tmplist)

print(list_a)

# 각 반의 합
a=[[67, 66, 65], [99, 98, 99], [34, 33, 32]]
list_h=[]
for i in range(3):
    s=0
    for j in range(3):
        s += list_a[i][j]
    list_h.append(s)
print("합:",list_h)

#평균
list_avg=[]
for i in range(3):
    tmp=list_h[i]/3
    list_avg.append(tmp)
print("평균:",list_avg)