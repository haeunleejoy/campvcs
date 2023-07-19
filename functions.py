def hello():
    name = input("name: ")
    print("Hello  " + name)
hello()

a = int(input("A "))
b = int(input("B "))
def sum(a,b):
    return a+b
c = sum(a,b)
d = 2 
e = sum(c,d)
print(e)

def duplicates(a,b,c,d):
    list=[a,b,c,d]
    for i in list:
        while list.count(i)>1:
            list.remove(i)
        return list 

# can say print or return(return is when I have to get something back from a previous code)

def calc(a,b):
    sum = a+b
    sub = a-b
    mult = a*b
    div = a/b
    return sum, sub, mult, div
print(calc(3,5))

# can say x = calc ... and say print x, then will print 

def list(*args):
    for i in args:
        print(i)
list(10,20)

def bye(name, age = 125):
    print("bye " + name)
    print(str(age)+ " years old") 
bye(name = "Ethan", age = 2)

def outer_fun(a,b):
    square = a ** 2  

    def addition (a,b):
        return a+b
    add = addition(a,b)
    return add + 7
print(outer_fun(4,6))