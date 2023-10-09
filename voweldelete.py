# program for delete vowel in given string
str=input("Enter the string:")
str2='aeiouAEIOU'
for i in str:
  if i not in  str2:
    print(i,end=" ")
