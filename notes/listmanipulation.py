# list manipulation now
# define your list

a = list(range(1,10))

print("a: ", a)

# first thing to get down is the basic list functions
# please remember them

# append
# add an item to the end of the list
a.append(11)
print("a got appended with a 11: ", a)

# set an item
# if you don't understand this expression, go to listindexing.py
a[8] = 10
print("a[8] got set to 10: ", a)

# pop an item
# popping removes the item, and also returns what it is
whatwelost = a.pop(-1) # -1 is a negative index to the LAST ITEM
print("a lost the last item: ", a, whatwelost)

# remove an item
# 'remove' removes the first occurence of whatever you put as a parameter
a.append(11)
a.remove(11)
print("a briefly had a 11 but check for me: ", a)

# extend me
# extending just adds a list ONTO your list
a.extend([99, 86, 43, 67])

print("a just welcomed new guys: ", a)

# list comprehension
# this just generates you a list in one expression
# the format is
# [<expression> for <iterator> in <list>]
# expression has to be any single command, it cannot be multiline
# iterator can be any variable name
# list has to be an actual list, or range()

b = [i ** 0.5 for i in range(10)] # return a list of square roots from sqrt(0) to sqrt(10)

print(b)

# deepcopy
b = [i for i in a]
print(b)

# using a function within it
def buzzfizz(number):
    if number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number

b = [buzzfizz(ite) for ite in a]
print(b)

"""
these are all of the functions you may need in the actual exam. there are some extras that are covered in
advancedlist.py incase you want to know a few 'shortcuts'
"""