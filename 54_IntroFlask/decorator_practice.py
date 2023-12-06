import time

def speed_calc_decorator(func):
    def wrapper_func():
        current_time = time.time()  # seconds since Jan 1st, 1970
        func()
        new_time = time.time()
        return new_time - current_time

    return wrapper_func
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

if __name__ == '__main__':
    print(slow_function())