def main():
    emoji = input("Let's make some emojis ")

    emoji = convert(emoji)

    print(emoji)

def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

main()