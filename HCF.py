#program for find HCF of given number:
a,b=map(int,input("Enter two numbers separate by space:").split(" "))
l=a if a>b else b
s=a if a<b else b
c=l%s
if(c==0):
  print("HCF is:",s)
else:
  while(c!=0):
    c1=c
    c=s%c
    if(c==0):
      print("HCF is:",c1)
