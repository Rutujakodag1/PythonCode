#Greater number between three numbers:
print("Enter three numbers:")
n=int(input())
m=int(input())
l=int(input())
if n>m and n>l:
  print("Greater is",n)
elif m>n and m>l:
  print("Greater is",m)
else:
  print("Greater is",l)
