###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
digits = digits[:3]
print(digits[:3])

def get_status(arr1, arr2):
    for i1 in range(3):
        for i2 in range(3):
            a1 = arr1[i1]
            a2 = arr2[i2]
            if i1 == i2 and a1 == a2:
                return "match"
            elif a1 == a2:
                return "close"
    return "nope"

def convert_to_int_array(inp):
    return [int(s) for s in str(inp)]

def determine_status(g):
    num_input = convert_to_int_array(g)
    if num_input == digits:
        return "full_match"
    return get_status(digits, num_input)

status = "started"
while status != "full_match":
    guess = input("What is your guess? ")
    status = determine_status(guess)
    if (status == "match"):
        print("You've guessed a correct number in the correct position")
    elif (status == "close"):
        print("You've guess a correct numberbut in the wrong position")
    elif (status == "nope"):
        print("You haven't guessed any of the numbers correctly")
    else:
        print("")

print("You have broken the code!")


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
