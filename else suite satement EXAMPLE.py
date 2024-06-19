group = [1,2,3,4,5]
search = int(input('Enter element to search:'))

for element in group: #1,2,3,4,5
   if search == element: 
      print('Element found in group') 
      break  
else: 
   print('Element not found in group') 


