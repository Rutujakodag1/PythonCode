#Fibonacci series:
n=int(input("Enter size of series"))
first=0
second=1
print(first)
print(second)
for i in range(n-2):
  next=first+second
  print(next)
  temp=first
  first=second
  second=next
