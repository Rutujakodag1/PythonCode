//Anagram or not
str1=input("Enter the string:")
str2=input("Enter the string:")
l3=0
l4=0
len1=len(str1)
len2=len(str2)
if len1==len2:
  for i in str1:
    if i in str2:
      l3=l3+1

  for i in str2:
    if i in str1:
      l4=l4+1


if l3==len1 and l4==len2:
  print("It is anagram")
else:
  print("It is not anagram")
