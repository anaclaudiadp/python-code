def mean(numbers):
    
    if type(numbers) == dict:
        return sum(numbers.values()) / len(numbers)
    else:
        return sum(numbers) / len(numbers)
    

# check if values in the numbers are all numbers (int or float)


# using isinstance() function to check the type
# it's better to use the isinstance() function rather than the type() 
# to check if an object is of a certain type
def mean_inst(numbers):
    
    if isinstance(numbers, dict):
        return sum(numbers.values()) / len(numbers)
    else:
        return sum(numbers) / len(numbers)
    
    
def mean2(*args):
    return sum(args) / len(args)
    

