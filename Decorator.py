def decorator(func):
    def wrapper():
        print("Before calling the function")

        func()

        print("After calling trhe function")
    return wrapper
    
@decorator
def hello():
    print("Hello Akash")

hello()
