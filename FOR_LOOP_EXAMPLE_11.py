sentence = "students flock to the arb for a riety of outdoor activities such as jogging and picnicking"
same_letter_count = 0
for i in sentence.split():
    if i[0]==i[-1]:
        same_letter_count+=1
print(same_letter_count)    
    
