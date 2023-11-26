number_str = input("Type an integer: ")
try:
    number = int(number_str)
    is_even = (number % 2) == 0
    if is_even:
        print(f"The number {number:.0f} is even")
    else:
        print(f"The number {number:.0f} is odd")
        
except:
    print("This is not an Integer")