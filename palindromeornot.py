#Palindrome or not 
str1=input("Enter the string:")
str2=''
for i in str1:
  str2=i+str2
print(str2)
if str1==str2:
  print("string is palindrome")
else:
  print("string is not palindrome")
