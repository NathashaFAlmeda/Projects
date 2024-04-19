def add(a,b):
    return a+b
def diff(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("division by zero is not possible")
        return None
    return a/b

def user_input():
    while True:
        try:
           a=int(input("enter the first number :"))
           b=int(input("enter the second number :"))
           return a,b
        except ValueError:
            print("Please enter integers.")
        
def calculator ():
    while True:
        print("1-Addition")
        print("2-Subtraction")
        print("3-Multiplication")
        print("4-division")
        select=int(input("choose the operation :"))
        if select=='1':
           a,b=input()
           result=add(a,b)
           print(f"The result is {result}")
        elif select=='2':
             a,b=input()
             result=diff(a,b)
             print(f"The result is {result}")
        elif select=='3':
             a,b=input()
             result=mul(a,b)
             print(f"The result is {result}")
        elif select=='4':
             a,b=input()
             result=div(a,b)
             print(f"The result is {result}")
             break
        else:
             print("PLease enter a valid operation")
if __name__=="__main__":
    calculator()
    
   


        
   
