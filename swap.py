#Swapping without using third variable
n,m=input("Enter the number:").split()
n=int(n)
m=int(m)
print("\nBefore swap \nfirst number: ",n)
print("second number:",m)
n=n+m
m=n-m
n=n-m
print("\nAfter swap \nfirst number:",n)
print("second number:",m)
