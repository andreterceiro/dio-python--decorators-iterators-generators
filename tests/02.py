def my_decorator(func):
    print("before")
    def internal():
        print("I am inside the internal function - 1")
        func()
        print("I am inside the internal function - 2")
    print("after")
    return internal

def another_function():
    print("I am inside the another function")

dec = my_decorator(another_function)
dec() # I need to execute the returned function!