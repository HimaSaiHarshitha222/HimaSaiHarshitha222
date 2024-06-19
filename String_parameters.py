s = input("Enter a String: ")
ca = ua = la = cd = spch = 0

for ch in s:#J,a,m,e,s, ,B,o,n,d,@,0,0,7
    if ch.isalpha():
        ca += 1
        if ch.isupper():
            ua += 1
        else:
            la += 1
    elif ch.isdigit():
        cd += 1
    else:
        spch += 1
 
print("No of Characters: ",len(s))
print("No of Words: ", len(s.split()))
print("No of Alphabets: ",ca)
print("No of Uppercase Alphabets: ",ua)
print("No of Lowercase Alphabets: ",la)
print("No of Digits: ",cd)
print("No of Special Characters: ",spch)
