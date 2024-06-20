from datetime import * 
d = date(day = 29, month = 4, year = 2020) 
t = time(15, 30) 
dt = datetime.combine(d, t) 
print(dt)
