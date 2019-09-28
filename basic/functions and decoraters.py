# using functions as parameters

def calculate(func,x):
    print("Ich berechne Dinge. In diesem Fall: '"+ func.__name__, end="' ") #name refers to function name(identifeier)
    print("von ", end=" ")
    print(x)
    return func(x)

def square(x):
    return x*x

print(calculate(square,5))

# decorater to modify functions

from math import sin, cos

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

sin = our_decorator(sin)
cos = our_decorator(cos)

for f in [sin, cos]:
    f(3.1415)

# decorater with parameters to alternate different outputs

def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator

@greeting("καλημερα")        
def foo(x):                                                     
    print(42)


# Alternative Schreibweise zu "@greeting("καλημερα")" !NACH FUNKTIONSDEKLERATION!

# greeting2 = greeting("καλημερα")
# foo = greeting2(foo)

foo("Hi")


    
