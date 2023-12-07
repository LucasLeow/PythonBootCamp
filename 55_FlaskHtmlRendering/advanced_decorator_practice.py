inputs = eval(input())

def log(func):
    def logger(*args, **kwargs):
        if len(args) > 0:
            print(f'You called {func.__name__}({args[0]}, {args[1]}, {args[2]})')
            print(f'It returned {func(args[0], args[1], args[2])}')

    return logger
@log
def a_function(a, b, c):
    return a * b * c

a_function(inputs[0], inputs[1], inputs[2])