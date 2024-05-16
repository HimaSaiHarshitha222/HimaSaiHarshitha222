num = int(input('enter a  week number:'))
week = {1:'sunday',2:'monday',3:'tuesday',4:'wednesday',5:'thursday',6:'friday',7:'saturday'}
if 1<=num<7:
    print(week[num])
else:
    print("not a week number")
