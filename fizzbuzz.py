x = int(input("Number: "))

def fizzbuzz(x):
    if x%3 == 0 : print("fizz")
    if x%5 == 0 : print("buzz")
    # can do the three things I want to do with two if statements, without elif statements

fizzbuzz(x)