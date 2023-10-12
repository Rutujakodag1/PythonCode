#lexicographic list
if __name__ == '__main__':
  x,y,z=map(int,input("Enter three numbers separate by space:").split(" "))
  n=int(input("Please enter the number you do not want to include in the sum:"))
li=[]
for i in range(0,x+1):
  for j in range(0,y+1):
    for k in range(0,z+1):
      if (i+j+k) != n:
          li.append([i,j,k],)
print(li)
    
