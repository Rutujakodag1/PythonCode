print(" \n             ★ REPORT CARD ★")
name=str(input("\n•Student Name:"))
t=str(input("•roll no:"))
s=str(input("•class:"))
print("********************************************************")
print("\n*Marks Out of 100*        ")
a=int(input("\nMarks of M-I:"))
b=int(input("Marks of BCME:"))
c=int(input("Marks of EM:"))
d=int(input("Marks of UHV:"))
e=int(input("Marks of EP:"))
f=a+b+c+d+e
g=(a+b+c+d+e)/500*100
print("\n\n")
print("=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=")
print("**              ★ ANNUAL REPORT CARD ★            **")
print("=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=")
print(   "STUDENT NAME:",name         )
print(   "CLASS:",s)
print(   "ROLL NO:",t               )
print("*****************************************************")
print("**   SUB   **   MARK OBTAINED   **   MARK OUT OF   **")
print("*****************************************************")
print("\n** M-I     **       ",a,"       **         100     **")
print("-----------------------------------------------------")
print("** BCME    **       ",b,"       **         100     **")
print("-----------------------------------------------------")
print("** EM      **       ",c,"       **         100     **")
print("-----------------------------------------------------")
print("** UHV     **       ",d,"       **         100     **")
print("-----------------------------------------------------")
print("** EP      **       ",e,"       **         100     **")
print("*****************************************************")
print("** TOTAL   **       ",f,"      **         500     **")
print("-----------------------------------------------------")
print("**   PERCENTAGE:     **           ",g,"%         **")
print("=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=")
