from abc import * 
class Myclass(ABC): 
   @abstractmethod 
   def connect(self): 
      pass 
   @abstractmethod 
   def disconnect(self): 
      pass
class Oracle(Myclass): 
   def connect(self): 
      print('Connecting to Oracle database...') 
   def disconnect(self): 
      print('Disconnected from Oracle.') 
class Sybase(Myclass): 
   def connect(self): 
      print('Connecting to Sybase database...') 
   def disconnect(self):  
      print('Disconnected from Sybase.') 
class Database: 
   str = input('Enter database name:') 
   classname = globals()[str] 
   x = classname() 
   x.connect() 
   x.disconnect()
