def stars(func):
    def wrapper():
        print('*********************')
        func()
    return wrapper

def hello():
    print("Hello World!")

@stars
def hello1():
    print("Hello World!")

hello()
stars(hello)()
hello1()
