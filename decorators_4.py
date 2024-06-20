def decor(fun): 
    def inner(): 
        value = fun()
        return value**2+5
    return inner 

@decor
def num():
    return 10  

print(num())  
