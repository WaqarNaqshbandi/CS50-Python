# Comments are used to write psuedocode, jus write what program should do and what steps should it take to do that. So when you are writing the program its easier to just get a reference to what the heck you were actually trying to do.
#docs.pythong.org
# / is an escape character, use it to write stuff that would normally be a part of syntax such as ""
# Ask user for their location
location = input("Hello, Where do you live? ")

# When you use a coma to add a new argument you will get a space in between, if you use + you won't, if you wanna remove the space when using commas you use the parameter sep="" just like end=""
# Show their location
print("I'm coming to "+location+", I know it's what everybody does so stop grinning.")

#here's how you remove a new line when using two functions on two separarte line.
name = input("What's your name? ")
print("You're dead ", end="")
print(name)

# Now the most recent way, an f string
print(f"hello, {name}")