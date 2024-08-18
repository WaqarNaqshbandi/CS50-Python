# Chain functions / methods
name = input("What's your name? ").strip().capitalize().title()

""" Remove spaces, use strip function/method for a string
name = name.strip()

# Capitalize, only capitalizes the first word.
name = name.capitalize()

Titlecase, capitalizes every word
name = name.title() 

Split
first, last = name.split(" ") The space in quotes means, we split wherever space comes in. first, last now become new variables taken out of the name after it's split.
"""

print(f"hello, {name}")