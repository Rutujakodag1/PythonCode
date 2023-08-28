#Binary conversion of given number
a=int(input("Enter the number:"))
n=a
li=[]
while a!=0:
  li.append(a%2)
  a=a//2
li.reverse()
print("Binary of ",n,"is:",end='')
for i in li:
  print(i,end='')
