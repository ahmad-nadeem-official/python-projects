import math

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b ==0 :
        print("syntax error")
    else:
        return a/b
        
if __name__ == "__main__":  #here i have add this, so it would not tease other code if i use it as a module
   
    numa = int(input("enter your 1st number "))        
    op = input("choose the operator ")
    numb = int(input("enter your 2nd number "))

    if op == "+" :
        print(add(numa,numb))
    elif op == "-":
        print(subtract(numa, numb))
    elif op == "*":
        print(multiply(numa,numb))
    else:
        print("syntax error")    
