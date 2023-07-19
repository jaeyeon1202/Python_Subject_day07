i=1 #초기식
while i<=5: #조건식
     print(i, end="")
     i += 1 #증감식
print("")
print(i)

n=1
s=0
while n <=10:
     if n % 2==0:
          s += n
     n += 1
print("s:",s)
 
n=2 #초기식
s=0
while n<=10: #조건식
     s += n #증감식
     n +=2
print("짝수합:",s)

n=9 #초기식
s=0
while n>=1: #조건식
     s+=n
     n -= 2 #증감식
print("홀수합:",s)