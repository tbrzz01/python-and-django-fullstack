def my_func(param1, param2='default'):
    """
    This is the docstring
    """
    print('my first python function')

def hello():
    return "hello"

result = hello()

print(my_func(1))

print(result)


# Lambda expression

# Filter
mylist = [1,2,3,4,5,6,7,8]

evens = filter(lambda (num): num % 2 == 0, mylist)
print(evens)

print('x' in mylist)
print(5 in mylist)
