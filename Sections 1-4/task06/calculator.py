def get_float_number():
    while True:
        try:
            input_value = float(input("Type a decimal number: "))
            return input_value
        except:
            print("Pleasse enter a valid decimal number! ")

def get_operator():
    while True:
        try:
            operator = input("Type the operator (+, -, *, /) : ")
            if operator in ['+', '-', '*', '/']: return operator
        except ValueError:
            print("Pleasse enter a valid operator ")

def calculate():
    first_value = get_float_number()
    secound_value = get_float_number()
    operator = get_operator()
    result = None
    if(operator == '+'):
        result = first_value + secound_value
    elif (operator == '-'):
        result = first_value - secound_value
    elif (operator == '*'):
        result = first_value * secound_value
    else:
        if(secound_value == 0):
            print("Error: Division by 0. ")
            return
        else:
            result = first_value / secound_value
    print(f"The result of {first_value} {operator} {secound_value} is {result}")
    
calculate()