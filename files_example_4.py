f =open("naveen.txt","w")
while True:
    name = input("Enter Name:")
    if name=='e':
        break
    f.write(name+"\n")
f.close()
