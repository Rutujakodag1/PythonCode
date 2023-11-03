#hackerrank logo
thickness = int(input())
c = 'H'
for i in range(1,(2*thickness+1)-1,2):
    print((c*i).center((2*thickness)-1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6-1))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6-1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6-1))

for i in range(0,(2*thickness+1)-1,2):
    print(((c*(2*thickness-i-1)).center((2*thickness)-1)).rjust(thickness*6-1))
