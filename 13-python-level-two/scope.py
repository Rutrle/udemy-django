x = 25


def my_func():
    x = 50
    #global x
    # return x

    def func_in():
        print(x)

    func_in()


print(x)
my_func()
