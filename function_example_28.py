def display(lst): 
 for i in lst: 
     print(i.lstrip()) 

lst = [x for x in input('Enter strings separated by comma:').split(',')] 
display(lst)
