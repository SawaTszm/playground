def say_hello(name=None):
    greeting = "Hello"
    greeting = greeting + f", {name}" if name else greeting
    print(greeting)
