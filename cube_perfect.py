x = int(input ('enter an number: '))

ans = 0
while ans**3 < x:
    ans += 1
if ans**3 != x:
    print (str(x) + " " + 'is not a perfect cube')
else:
    print ('Cube root of' + " " + str(x) + " " + 'is' + " " + str(ans))
