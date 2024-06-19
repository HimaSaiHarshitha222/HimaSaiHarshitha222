def display(**kwargs): 
   for x, y in kwargs.items():
     print('key = {}, value = {}'.format(x, y)) 


display(force = 456.78, acc = 7.98) 
