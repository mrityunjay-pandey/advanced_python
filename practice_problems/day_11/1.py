# def outerFunction(text):
#     text = text
#     def innerFunction():
#         print(text)
#     return innerFunction
# myFunction = outerFunction('Hey!')
# myFunction()


# def decor(func):
#     def inner():
#         print("-------------------")
#         func()
#         print("--------------------")
#     return inner

# def msg():
#     print("Python Programming")

# pqr = decor(msg)
# pqr()

# from datetime import datetime
# from playsound import playsound

# def not_during_night(func):
#     def inner():
#         if 7 <= datetime.now().hour < 22:
#             func()
#             playsound(sound_file)
#         else:
#             print("Sorry! Unable to play music in night")
#     return inner

# @not_during_night
# def music():
#     print("Playing music")


# sound_file = 'C:\\Users\\Raja Pandey\\Desktop\\emergency-alarm-with-reverb-29431.mp3'




# music()

def do_twice(func):
    def wrapper_do_twice(*args, **kargs):
        func(*args, **kargs)
        func(*args, **kargs)
    return wrapper_do_twice

@do_twice
def message(name):
    print(f"Hello {name}")

message("Mohit")

def do_twice(func):
    def wrapper_do_twice(*args, **kargs):
        func(*args, **kargs)
        func(*args, **kargs)
    return wrapper_do_twice

@do_twice
def message(name):
    print(f"Hello {name}")

message("Mohit")

def do_twice(func):
    def wrapper_do_twice(*args,)