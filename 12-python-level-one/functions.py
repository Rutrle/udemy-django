def my_func(param1='default'):
    """
    THIS IS DOCSTRING
    """
    print(f'my first python function{param1}')


my_func()
my_func("")


def hello():
    print("hello")
    return "hello"


result = hello()
print(result)

# Lambda Expression

# Filter
mylist = [1, 2, 3, 4, 5, 6, 7]


def even_bool(num):
    return num % 2 == 0


evens = filter(even_bool, mylist)
print(list(evens))


# => typicall usage for lambda
evens = filter(lambda num: num % 2 == 0, mylist)
print(list(evens))

print('x' in ['2', 1, 'x'])
