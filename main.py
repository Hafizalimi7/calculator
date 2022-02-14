from art import logo


def welcome():
    print('Welcome to the Calculator')

welcome()

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def division(x,y):
    return x / y

operators = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':division
}

def good_bye():
    print('See you next time.')
    calculator()

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: \n"))
    for symbol in operators:
        print(symbol)
    
    should_cont = True

    while should_cont:
        operation_symbol = input('pick an operator\n')
        num2 = float(input("What's the second number?: \n")) 
        calc_func = operators[operation_symbol]
        answer = calc_func(num1,num2) 
        print(f"{num1} {operation_symbol} {num2} = {answer}")
      
        if input(f"Type 'y' if you want to use the {answer} to continue or  type 'no' to quit") == 'y':
            answer = num1
        else:
            should_cont = False
            good_bye()


calculator() 