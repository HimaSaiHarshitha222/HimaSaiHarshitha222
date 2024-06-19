a = (10,20,30,40,50,60,70)
pos = int(input("Enter Position Number to modify an Element: "))
ele = int(input("Enter Element: "))

left = a[:pos-1]
right = a[pos:]
ans = left + (ele,) + right
print(ans)
