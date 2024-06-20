class NaveenError(Exception): 
   def __init__(self, arg): 
      self.msg = arg

def check(dict): 
      for k,v in dict.items(): 
         print('Name= {:15s} Balance= {:10.2f}'.format(k,v)) 
         if(v<2000.00): 
            raise NaveenError('Balance amount is less in the account of '+k) 

bank = {'Raj':5000.00, 'Vani':8900.50, 'Ajay':1990.00, 'Naresh':3000.00} 

try: 
  check(bank) 
except NaveenError as me: 
  print(me)
