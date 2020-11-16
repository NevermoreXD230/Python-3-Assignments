### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
def openLocks(number_of_lockers , number_of_students):
    if type(number_of_lockers) == str or type(number_of_students) == str or number_of_lockers < 0 or number_of_students <0:
        return None
    if number_of_lockers == 0 or number_of_students == 0:
        return 0
    
    
    locks = [1] * number_of_lockers # in this closed locker means lock[0] and open mean lock[1]
    
    open_locks = 0
    
    for students in range(1 ,number_of_students+1):
        
        for lockers in range(1 , number_of_lockers+1):
            
            if lockers % students == 0:
                
                if students > 1:
                    
                    if locks[lockers - 1] == 1:
                        
                        locks[lockers - 1] = 0
                    else:
                        locks[lockers - 1] = 1
                
    for openlocks in range(1 , number_of_lockers+1):
        
        if locks[openlocks-1] == 1:
            
            open_locks += 1
    
    return open_locks


#### End OF MARKER





### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###
def mostTouchableLocker(number_of_lockers , number_of_students):
    x = 0
    z = 0
    if number_of_lockers < 0 or number_of_students < 0:
        return None
    if number_of_lockers == 0 or number_of_students == 0 :
        return 0
    
    if number_of_lockers < number_of_students or number_of_lockers%number_of_students == 0:
        
        for lockers in range(1 , number_of_lockers+1):
            y = 0
            for i in range(1 , lockers+1):
            
                if lockers % i == 0:
                
                    y+=1
        
                if y >= x:
                    x = y
            
            if y >= x:
            
                z = lockers
        return z
    else:
        
        for lockers in range(1 , number_of_students+1):
            y = 0
            for i in range(1 , lockers+1):
            
                if lockers % i == 0:
                
                    y+=1
        
                if y >= x:
                    x = y
            
            if y >= x:
            
                z = lockers
        return z
#### End OF MARKER


