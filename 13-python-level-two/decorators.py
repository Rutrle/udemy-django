s = "Global variable!"


def func():
    global s
    s = 50
    print(s)


def func2():
    mylocal = 10
    print(locals())
    print(globals())


func()
print(s)
func2()

"""
def hello(name="Jose"):
    
    return "Hello " + name


print(hello())

mynewgreet = hello #assigning function

print(mynewgreet())
"""


def hello(name="jose"):
    print("the hello() function has been run")

    def greet():
        return "this string is inside greet()"

    def welcome():
        return "this string is inside welcome!"

    if name == "jose":
        return greet
    else:
        return welcome


x = hello()

print(x())


def second_hello():
    return "Hi JOSE!"


def other(func):
    print("Hello")
    print(func())


other(second_hello)


def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC HSD BEEN CALLED")

    return wrap_func


#def func_needs_decorator():
#    print("THIS FUNCTION IS IN NEED OF A DECORATOR")


#func_needs_decorator = new_decorator(func_needs_decorator)

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR")


    
func_needs_decorator()
