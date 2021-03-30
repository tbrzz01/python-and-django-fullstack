x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())
my_func()
print(x)


# Local
lambda x: x**2

# Enclosing function locals
name = 'This is a global name!'

def greet():
    name = "sammy"
    def hello():
        print("hello" + name)
    hello()

greet()


y = 10
def func():
    global y;
    y = 200;

print("y before func call", y)
func()
print("y after func call", y)
