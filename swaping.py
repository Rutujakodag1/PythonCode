#Swaping number using third variable
n,m=input("Enter the number:").split()
n=int(n)
m=int(m)
print("\nBefore swap \nfirst number: ",n)
print("second number:",m)
l=m
m=n
n=l
print("\nAfter swap \nfirst number:",n)
print("second number:",m)
