#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) returns True
# arrayCheck([1, 1, 2, 4, 1]) returns False
# arrayCheck([1, 1, 2, 1, 2, 3]) returns True

def arrayCheck(nums):
    return len(filter(lambda l: l == True, [nums[i:i+3] == [1,2,3] for i in range(len(nums))])) > 0

print(arrayCheck([1,1,2,3,1]))
print(arrayCheck([1,1,2,4,1]))
print(arrayCheck([1,1,2,1,2,3]))


#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') returns 'Hlo'
# stringBits('Hi') returns 'H'
# stringBits('Heeololeo') returns 'Hello'

def stringBits(stri):
    return stri[0::2]

print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') returns True
# end_other('AbC', 'HiaBc') returns True
# end_other('abc', 'abXabc') returns True


def end_other(a, b):
    lower_a = a.lower()
    lower_b = b.lower()
    e = lambda la,lb: la[len(la)-len(lb):len(la)] == lb
    return e(lower_a, lower_b) or e(lower_b, lower_a)

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') returns 'TThhee'
# doubleChar('AAbb') returns 'AAAAbbbb'
# doubleChar('Hi-There') returns 'HHii--TThheerree'

def doubleChar(str):
    new_str = ''
    for s in str:
        new_str += s + s
    return new_str

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))



#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) returns 6
# no_teen_sum(2, 13, 1) returns 3
# no_teen_sum(2, 1, 14) returns 3

def no_teen_sum(a, b, c):
    # This could definitely be cleaner - doing too many rnages in helper function
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in range(13, 15) or n in range(17, 20):
        return 0
    return n

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) returns 3
# count_evens([2, 2, 0]) returns 3
# count_evens([1, 3, 5]) returns 0

def count_evens(nums):
    return len(filter(lambda x: x%2 == 0, nums))

print(count_evens([2,1,2,3,4]))
print(count_evens([2,2,0]))
print(count_evens([1,3,5]))

