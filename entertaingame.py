#Entertaining game
bill=0
height=int(input("Enter the height in cm:"))
if height>120:
  print("You can ride")
  age=int(input("Enter your age:"))
  if age<12:
    bill+=5
  elif age<18:
    bill+=7
  else:
    bill+=12
  photo=input("Do you want photos(y/n):")
  photo.lower()
  if photo=='y':
    bill+=3
    print(f"Total bill {bill}")
  else:
   print(f"Total bill {bill}")
else:
  print("cant ride")
    
