name = input("What's your name?")
age = input("How old are you?")

if name and age:
    print(f"Your name is {name}")
    print(f"Your name inverted: {name[::-1]}")
    if ' ' in name:
        print("Your name has space(s)")
    else:
        print("Your name does not have spaces")
    print(f"Your name has {len(name)} characters")
    print(f"The first letter of your name is {name[0]}")
    print(f"The last letter of your name is {name[-1]}")
else: 
    print("Sorry, empty fields...")