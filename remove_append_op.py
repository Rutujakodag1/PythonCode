#program for removing all zero and append all zero:
s=[]
s=list(map(int,input().strip().split()))
for i in range(s.count(0)):  
  s.remove(0)
  s.append(0)
print(s)
