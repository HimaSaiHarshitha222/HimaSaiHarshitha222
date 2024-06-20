from datetime import * 
group = [] 
group.append(date.today()) 

d = date(2015, 6, 29) 
group.append(d)

d = date(2014, 6, 30) 
group.append(d) 

group.append(d+timedelta(days=25)) 
 
group.sort(reverse = True) 
for d in group: 
   print(d)
