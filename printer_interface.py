from abc import * 
class Printer(ABC): 
   @abstractmethod 
   def printit(self, text): 
      pass 
   @abstractmethod 
   def disconnect(self): 
      pass 
class IBM(Printer): 
   def printit(self, text): 
      print(text) 
   def disconnect(self): 
      print('Printing completed on IBM printer.') 
class Epson(Printer): 
   def printit(self, text): 
      print(text) 
   def disconnect(self): 
      print('Printing completed on Epson printer.') 
class UsePrinter:
   str = input()
   classname = globals()[str] 
   x = classname() 
   x.printit('Hello, this is sent to printer') 
   x.disconnect()
