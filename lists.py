food = ['pizza', 'chicken', 'fries']
numbers = [1, 2, 3]
mixed = ['pizza', 1, 'chicken', 2]

drinks = ['coke', 'smoothie', 'sprite']
menu = food + drinks
print(menu)

# changing lists
menu. remove('chicken')
print(menu)

menu. append ('pasta')
print(menu)

# when inserting in beginning
menu.insert(0, 'Hamburger')
print(menu)

# when deleting the last thing (do not know what it is)
menu.pop(6)
print(menu)

# sort list 
menu.sort()
print(menu)

menu.reverse()
print(menu)

# splice list
print(menu[0])
print(menu[:2])

if "ice cream" in menu: 
    print('Sophie is happy')
else:
    print('Sophie is sad')
food1 = input('food1: ')
food2 = input('food2: ')
food3 = input('food3: ')

order = []
order.append(food1)
order.append(food2)
order.append(food3)

print(order)

jellyctr = order.count('jelly')
print(jellyctr)

#chaning the order of the last and first
set = ['pencil', 'eraser', 'notebook', 'backpack']
# homework q: how to swap that

# check for duplicates
set = ['pencil', 'eraser', 'notebook', "notebook"]
count = 3
count = 2
count = 1 

while set.count("notebook") > 1: 
    set.remove("notebook")
    print(set)

for []
# homework inserting text inside the square brackets