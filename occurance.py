#Occurance of given character in string
str1=input("Enter the string:")
ch=input("Enter the character:")
flag=0
for i in str1:
  if i==ch:
    flag=flag+1

print(flag)
