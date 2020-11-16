### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
def chocolatePrice(ali_budget,bashir_budget):
    
    if ali_budget == 0:
        return ali_budget
    
    if bashir_budget== 0:
        return bashir_budget
    
    if ali_budget == bashir_budget:
        return ali_budget
    
    if ali_budget > bashir_budget:
        
        return chocolatePrice(ali_budget-bashir_budget , bashir_budget)
    else:
        return chocolatePrice(ali_budget , bashir_budget-ali_budget)

#### End OF MARKER





### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###
def calculateProfit(ali_budget , bashir_budget):
    
    if type(ali_budget) == str or type(bashir_budget) == str or ali_budget == 0 or bashir_budget == 0:
        
        return "Not Possible"
    if ali_budget < 0 or bashir_budget < 0:
        return "Not Possible"
    
    if type(ali_budget) == float or type(bashir_budget)== float:
        
        ali_budget = int(ali_budget)
        
        bashir_budget = int(bashir_budget)
        
    
    ali_choco = ali_budget / chocolatePrice(ali_budget , bashir_budget)
        
    bashir_choco = bashir_budget / chocolatePrice(ali_budget , bashir_budget)
        
    if ali_choco > bashir_choco:
        
        ali_profit = ((ali_choco * chocolatePrice(ali_budget , bashir_budget))*(3/2)) - ali_budget
    else:
         ali_profit = ((ali_choco * chocolatePrice(ali_budget , bashir_budget))*2) - ali_budget
     
    if bashir_choco > ali_choco:
        
        bashir_profit = ((bashir_choco * chocolatePrice(ali_budget , bashir_budget))*(3/2)) - bashir_budget
    
    else: 
        bashir_profit = ((bashir_choco * chocolatePrice(ali_budget , bashir_budget))*2) - bashir_budget
    
    if ali_profit > bashir_profit:
        
        return ali_profit
    
    else:
        return bashir_profit

#### End OF MARKER


