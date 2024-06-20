




from datetime import * 

dt = date.today()
print("Yesterday's Date:",dt-timedelta(days=1))
print("Today's Date:",dt)
print("Tomorrow's Date:",dt+timedelta(days=1))
