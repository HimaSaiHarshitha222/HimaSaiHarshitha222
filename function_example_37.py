lst1 = [1, 2, 3, 4, 5] 
lst2 = [10, 20, 30, 40, 50] 
lst3 = list(map(lambda x, y: x*y, lst1, lst2)) 
print(lst3)
