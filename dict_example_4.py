str = "Sujay=23, Rajesh=20, Lahari=19,Nithin=22"
l = []
for ele in str.split(','):
    l.append(ele.split('='))
    print(l)

print(dict(l))

