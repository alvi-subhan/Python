inp=int(input("enter the number for factorial "))
#add_on=0
def factorial(inp):
    if inp==0:
        return 1
    return inp * factorial(inp-1)
print(factorial(inp))