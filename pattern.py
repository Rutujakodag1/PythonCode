#Pattern
num=int(input("Enter number of rows:"))
for i in range(1,num+1):
  num=num-1
  print(" "*num,end="")
  print("* "*i)
