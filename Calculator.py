def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error! Division by zero is not alliance"
    return a/b
while True:
    print("\n====simple calculator====")
    print("1. addition")
    print("2 substraction")
    print("3. multiplication")
    print("4. division") 
    print("5. exit")

    choice= input("Enter the Choice(1-5):")

    if choice=="5":
        print("Thnkyou for using the calculator")
        break
    if choice in ("1","2","3","4"): 
        try:
            num1=float(input("Enter first number"))
            num2=float(input("Enter second number"))
            if choice=="1":
                print(f"Result:{add(num1,num2)}")
            elif choice=="2": 
                print(f"Result:{subtract(num1,num2)}")
            elif choice=="3":
                print(f"Result:{multiply(num1,num2)}")       
            elif choice=="4":
                print(f"Result:{divide(num1,num2)}")
        except ValueError:
            print("Invalid input! Please enter numeric value")
    else:
        print("Invalid choice! Please slect bteween 1 and 5.")    