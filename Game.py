#Game of kelvin and stuart
kelvin=input("Enter kelvin words:")
stuart=input("Enter stuart words:")
k=0
s=0
if kelvin[0]=='a' or kelvin[0]=='e' or kelvin[0]=='i' or kelvin[0]=='o' or kelvin[0]=='u' or kelvin[0]=='A' or kelvin[0]=='E' or kelvin[0]=='I' or kelvin[0]=='O' or kelvin[0]=='U':
  k+=1
if stuart[0]=='a' or stuart[0]=='e' or stuart[0]=='i' or stuart[0]=='o' or stuart[0]=='u' or stuart[0]=='A' or stuart[0]=='E' or stuart[0]=='I' or stuart[0]=='O' or stuart[0]=='U':
  s+=1
if k==0 and s==1:
  print("stuart win")
elif k==1 and s==0:
  print("Kelvin win")
elif k==0 and s==0:
  print("Game stop")
else:
  print("Game tie")
