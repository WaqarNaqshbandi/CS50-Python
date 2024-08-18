# Integers are without decimals, floats are with decimals

"""x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")
"""

x = float(input("What's x? "))
y = float(input("What's y? "))

# ,2 here is ndigits (number of digits)
z = round(x / y, 2)

print(z)