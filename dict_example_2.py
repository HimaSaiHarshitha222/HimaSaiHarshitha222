x = {} 
n = int(input('How many players?')) 

for i in range(n): 
   k = input('Enter player name:') 
   v = int(input('Enter runs:'))
   x.update({k:v})
   
print('\nPlayers in this match:') 
for pname in x.keys(): 
   print(pname) 
name = input('Enter player name:') 
runs = x.get(name, -1) 
if(runs == -1): 
   print('Player not found') 
else: 
   print('{} made runs {}.'.format(name, runs))
