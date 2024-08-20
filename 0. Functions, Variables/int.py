# Not a real calculator yet.
#Use int function to convert your strings to integers

"""x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)"""

""" You can nest functions like this
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)"""

# Here's how you can use your own functions properly. x23 is our custom function and x is parameter inside it. x = int.... means that we are defining x above the function so the function knows what value to use inside the parameter
def main():
    x = int(input("What's X? "))
    print("X -23 is ", x23(x))

# x23 is the function and n is the vale / parameter. We return the parameter - 23
def x23(n):
    return n - 23

main()