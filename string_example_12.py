#12) Write a Python Program to remove duplicates in the given String.

s = input("Enter a String: ").lower()
ans = ''

for ch in s:#n,a,v,e,e,n
    if ch not in ans:
        ans = ans + ch
print(ans)
