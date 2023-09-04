#Game
kelvin=input("Enter kelvin words:")
stuart=input("Enter stuart words:")
k=0
s=0
str1='aeiouAEIOU'
if kelvin[0] in str1:
  k+=1
if stuart[0] in str1:
  s+=1
if k==0 and s==1:
  print("stuart win")
elif k==1 and s==0:
  print("Kelvin win")
elif k==0 and s==0:
  print("Game stop")
else:
  print("Game tie")
