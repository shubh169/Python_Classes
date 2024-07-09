from logo import logo
print(logo)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multifly(a,b):
    return a*b
def divide(a,b):
    return a/b

operations={
            "+":add,
            "-":subtract,
            "*":multifly,
            "/":divide
            }

def calculator():
    print(logo)
    num1=float(input("What's the first number?:"))
    is_continue=True
    while is_continue:
        for key in operations:
            print(key)
        operation_symbol=input("Pick an operation from the line above:")
        num2=float(input("What's next number?:"))

        function=operations[operation_symbol]
        result=function(num1,num2)
        print(f"{num1}{operation_symbol}{num2}={result}")
        choice=input(f"type 'y' to continue calculating with {result} or type 'n' to start a new calcultion.").lower()
        if choice=='y':
            num1=result
        else:
            is_continue=False 
            calculator()   
            
calculator()