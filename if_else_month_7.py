num = int(input('enter a month number:'))
month = {1:'jan has 31 DAYS',2:'feb has 28/29 DAYS',3:'march has 31 DAYS',4:'april has 30 DAYS',5:'may has 31 DAYS',6:'june has 30 DAYS',7:'july has 31 DAYS',8:'august has 31 DAYS',9:'sep has 30 DAYS',10:'oct has 31 DAYS',11:'nov has 30 DAYS',12:'DEC has 31 days'}
if 1<=num<=12:
    print(month[num])
else:
    print("INVALID NUMBER")
