# Basics

'hello'
"hello"
"we're people"

mystring = 'abcdefg'
# SLICING
print(mystring[0])
print(mystring[4:])
print(mystring[:3])
print(mystring[2:5])
# every second string
print(mystring[::2])

# Basic String Methods
x = mystring.lower()
print(x);
x = mystring.upper()
print(x)
x = mystring.capitalize()
print(x)
x = mystring.split('e')
print(x)


# Print formatting
x = "Insert another string here: {}".format("INSERT ME!")
print(x)
x = "Item One: {x} Item Two: {y}".format(x = "dog", y = "cat")
print(x)
