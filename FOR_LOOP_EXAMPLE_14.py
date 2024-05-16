s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
num_vowels = 0
for i in s.split():
    if 'a' or 'e'or 'i' or 'o' or 'u' in i:
        num_vowels+=1
print(num_vowels)        
