# lists are simple but theres some things to remember for the exam

# we define a list EXPLICITLY via this
my_list = [0, 1, 2, 3, 4, 5, 6, 7]

print(my_list)

# the object for a list / the caster object for a list is literally just list()
a_list = list(range(1, 8))

print(a_list)

# the thing with lists, and not any other literal variable (like numbers, or strings)
# is this

a = [1,2,3,4,5,6,7]
b = a
b[2] = 9

print(a) # a will mirror the change we pushed to b

# call this a whatever, the technical term for it is b is being a pointer to a instead of just being the contents
# of a

# it is like a site redirecting you to another site
# you could have visited it directly but this is just a site that redirects you to it

# how do we fix this
# its called deep copying

# there are multiple ways to do it, here is my way
b = [i for i in a] # list comprehension
b[2] = 3

print(a, b) # these should be different now, well done, you have broken the tie between them

# there is a module to do it
import copy

c = [1,2,5]
d = copy.deepcopy(c)

d[2] = 9
print(c, d)

