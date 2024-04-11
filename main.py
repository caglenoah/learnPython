def remove_nonints(nums):
    integer = []
    for number in nums:
        if type(number) == int:
            integer.append(number)
    return integer
            
