a = (10,20,30,40,50,60,70)
pos = int(input("Enter Position Number to delete an Element: "))

left = a[:pos-1]
right = a[pos:]
ans = left + right
print(ans)
