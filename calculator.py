print("Welcome to Joy's calculator\n")

x = int(input("What is your first integer?"))
y = int(input("What is your second integer?"))

# get add, subtract, multiply or divide
math = input("What would you like to do with these numbers?")

# if add, subtract multiply or divide, compute answer
if math == "add":
    print(x+y)

elif math == "subtract":
    print(x-y)

elif math == "multiply":
    print(x*y)

elif math == "divide":
    print(x/y)
