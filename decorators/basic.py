from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("before the function runs")
        func()
        print("after the function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello! from the greet function.")


greet()

print(greet.__name__)  # Output: wrapper