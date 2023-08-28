#Prime factor of given number:
a=int(input("Enter the number:"))
for i in range(1,a+1):
  if a%i==0:
    flag=0
    for j in range(1,i+1):
      if i%j==0:
        flag=flag+1
    if flag==2:
      print(i)
