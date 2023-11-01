print("!!!  DOOR  MAT  !!!")
rows=int(input("\n\nEnter number of rows:"))
col=rows*3
str='WELCOME'
d='.|.'
print("\n\n")
for i in range(1,rows+1,2):
  print((d*i).center(col,'-'))
print(str.center(col,'-'))
for i in range(rows,0,-2):
  print((d*i).center(col,'-'))
