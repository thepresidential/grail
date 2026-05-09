# list indexing is fun
# not really but it gets better if you take some time to practice it

# start with a list
my_list = [i for i in range(127)]
print(my_list)
# this is a list from 0 to 126

# now, in python, all lists are ZERO indexed
# this means the first item is referenced to by the number 0

# how do we reference using a number?
print(my_list[0]) # < this should be 0 as the first item is 0

# negative indexing is also simple, but starts from the end
# it is '-1' indexed, -1 being the last item, -2 being the next, all the way to -len(list) being the first item
print(my_list[-1])

# we can slice a section of the list
print(my_list[0:6])
# note that this goes to that index, non-inclusive.
# the program will output all values up to index 5, not 6 (remember it is 0 indexed)

# if a slice starts from the beginning, or goes until the end, we can just drop the 0, or the last reference
print(my_list[:6]) # should output the same as the above
print(my_list[120:]) # outputs the last 7 items

# fancy stuff?
# so if you do this, it acts like a slice, but instead of counting up in 1s, it counts up in whatever
# number you put at the end
print(my_list[10:50:5])
print(my_list[5:60:10])

# here is a quick way to reverse a list too
print(my_list[::-1])
# notice how this works, it uses a slice from the beginning to the end via :, then steps by -1