from functools import wraps
from xml.parsers.expat import model

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Calling : {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished : {func.__name__}")
        return result
    return wrapper

@logging_decorator
def car(brand, variant="sports edition"):
    print(f"Car brand and variant: {brand} {variant}")

car("BMW")