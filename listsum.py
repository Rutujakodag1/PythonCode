//sum of elements in list
num=[]
n=int(input("Enter size of list:"))
for i in range(n):
  el=int(input())
  num.append(el)
sum=0
for i in num:
  sum=sum+i
print(sum)
