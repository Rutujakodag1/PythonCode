//Number is perfect or not
n=int(input("Enter the number:"))
flag=0
for i in range(1,n):
  if n%i==0:
    flag=flag+i
if flag==n:
  print("Number is perfect")
else:
  print("Number is not perfect")
