print("Welcome to contact list!!")
n=int(input("\nEnter the size:"))
names=[]
numbers=[]
flag=0
for i in range(n):
  name=input("\nEnter contact name:")
  names.append(name)
  num=int(input("Enter contact number:"))
  numbers.append(num)
search=input("\nsearch the contact:")
for i in range(len(names)):
  if search==names[i]:
    print("Contact found:",numbers[i])
    flag=1
if flag==0:
  print("Contact not found")
