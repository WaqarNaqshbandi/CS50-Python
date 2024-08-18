"""
You can define a function with def and then name the function, inside brackets you can leave empty or define a parameter with a custom name and then you can also assign it a default value if you want.
def hello(to="anonymous"):
    print("hello,", to)

hello()
name = input("What's your name? ")

Here we are calling the hellow function and adding name as a parameter, incase we didn't use parameter like on line 6, we would just get the default value of said parameter.
hello(name)

main is a standard practice to define a main function and the write everything inside it while creating your functions after the usecase as can be seen below."""

def main():

    hello()
    name = input("What's your name? ")

    hello(name)

def hello(to="anonymous"):
    print("hello,", to)

main()