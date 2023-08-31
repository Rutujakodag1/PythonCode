#Find LCM:
num1,num2=input("Enter the two number:").split()
num1=int(num1)
num2=int(num2)
if num1>num2:
  great=num1
else:
  great=num2
flag=0
while(flag==0):
  if great%num1==0 and great%num2==0:
    lcm=great
    flag=1
  great=great+1
print("LCM of",num1,"and",num2,":",lcm)
