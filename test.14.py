# sub=["국어","영어","수학"]
# h=[]
# sum=0
# for i in range(3):
#     score=int(input(sub[i]+"점수:"))
#     sum += i
# avg=sum/3

score=[]
s=0
for i in ["국어","영어","수학"]:
    tmp=int(input(i+"점수입력:"))
    score.append(tmp)
   
for i in range(len(score)):
    s += score[i]
print(score)
print("합:%d 평균:%.2f" % (s,s/len(score)))