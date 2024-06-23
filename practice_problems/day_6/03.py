def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

# Example usage
@start_end_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Calling the decorated function
say_hello("Alice")
