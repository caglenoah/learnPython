def is_prime(number):
    if number <= 1:
       return False
       
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True



     #write a for loop that starts at 2 and ends at number
    # have number % by i if there is a remainder move on to the next i
    #if there is no remainder stop loop and return false
    #if loop completes return true