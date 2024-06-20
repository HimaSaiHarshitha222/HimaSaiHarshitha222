f = open('naveen.txt', 'a+') 
print('Enter text to append(e at end):') 

while str != 'e': 
   str = input() 
   if(str != 'e'): 
     f.write(str+"\n") 

f.seek(4,0) 

print('The file contents are:') 
str = f.read() 
print(str) 
f.close()
