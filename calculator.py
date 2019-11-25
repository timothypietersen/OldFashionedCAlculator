import math

def calculator():
    num1 = float(input("FIRST NUMBER>> "))
    operator = input("""[OPERATORS: + :addition| - :subtraction| /:division| *: multiplication/power| %:square_root| @:round]
OPERATOR>> """)
    if operator == "%":
        result = math.sqrt(num1)
        print(result)
    elif operator == "@":
        result = round(num1)
        print(result)
    else:
        num2 = float(input("SECOND NUMBER>> "))
    result = 0
    if operator == "+":
        result = num1+num2
        print(result)
    elif operator == "-":
        result = num1-num2
        print(result)
    elif operator == "/":
        result = num1/num2
        print(result)
    elif operator == "*":
        power = input("Do you want the Power of these input [Y/N]>> ")
        if power == "Y":
            result = num1**num2
            print(result)
        else:
            result = num1*num2
            print(result)
    elif operator == "":
        print("NO OPERATOR CHOSEN")
    else:
        print("="*30)
calculator()