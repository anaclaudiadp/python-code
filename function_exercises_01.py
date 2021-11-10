# Function Exercises
#
#

# ## Exercise 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.

def check_ten(n1,n2):
    return (n1 + n2) == 10
    

# ## Exercise 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1,n2):
    if (n1+n2) == 10:
        return True
    else:
        return n1+n2



# ## Exercise 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.



def first_upper(mystring):
    return mystring[0].upper()



# ## Exercise 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".

def last_two(mystring):
    if len(mystring) < 2:
        return "Error"
    else:
        return mystring[-2:]


# ## Exercise 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list.


#fix it:
def seq_check(nums):
    seq = [1,2,3]
    seq_str = ''.join(str(seq))
    num = ''.join(str(nums))
    if seq_str in num:
        return True
        

#correct one:
def seq_check(nums):
    for i in range(len(nums)-2):
    #0,1,2,3,......, n-2
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False
  
    


# ## Exercise 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). 



def compare_len(s1,s2):
    return abs(len(s1) - len(s2))



# ## Exercise 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.



def sum_or_max(mylist):
    if len(mylist) % 2 == 0:
        return sum(mylist)
    else:
        return max(mylist)