#to calculate dearness allowance 
def da(basic): 
    da = basic*80/100
    return da 


#to calculate house rent allowance 
def hra(basic): 
    hra = basic*15/100 
    return hra 


#to calculate provident fund amount 
def pf(basic): 
    pf = basic*12/100
    return pf 


#to calculate income tax payable by employee 
def itax(gross): 
     tax = gross*0.1
     return tax

