def main():
    a = get_number("Input A:__")
    b = get_number("Input B:__")
    op = get_op()
    result = calculator(a,b,op)
    print(f"Result: {result}")
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Only number allow!")

def get_op():
    op_list = ["+", "-", "*", "/"]

    while True:
        op = input("Please enter the operation ")
        if op in op_list:
            return op
        else:
            print("Please only enter +_*/")
       
def calculator(a,b,op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a*b
    elif op == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
main()
