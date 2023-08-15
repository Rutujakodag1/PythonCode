#remove character from string
str1=input("Enter string:")
ch=input("Enter the character you want to remove:")
str2=''
for i in str1:
  if i!=ch:
     str2=str2+i

print(str2)
