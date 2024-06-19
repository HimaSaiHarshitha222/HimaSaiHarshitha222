#8) Write a Python program to find the maximum occurring character in a given string.

s = input("Enter a String: ")
maxi = 0
for ch in s:#s,a,r,e,g,a,m,a, ,p,a,d,a, ,n,e,s,a
    if s.count(ch)>maxi:
        max = ch
        maxi = s.count(ch)

print(max)
