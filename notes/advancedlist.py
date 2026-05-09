# if the first 3 list files were fine, here are some extra tricks

# list casting a set
# this removes all duplicates within a list
a = [i ** 2 for i in range(10)]
a[2] = 1
a[3] = 1
a[4] = 1

# alot of duplicates sadly
print(a)

# list cast a set
my_cleaned_up = list(set(a)) # does not retain order

print("a without duplicates: ", my_cleaned_up) # no duplicates!!

# sorting a set in ascending order
# my_cleaned_up is unsorted, lets sort it
print("Sorted and descending order sorted list: ")

my_cleaned_up = list(sorted(my_cleaned_up, reverse=False)) # reverse says do we do it in ascending, or descending

print(my_cleaned_up)

my_cleaned_up = list(sorted(my_cleaned_up, reverse=True))
print(my_cleaned_up)

# mapping
# mapping just applies a given function to every item of a list
# ignore the absolute confusion that are lambda functions and just look at how it is used within map
print("Mapped to sqrt x: ")
square_root = lambda x: x ** 0.5
print(list(map(square_root, my_cleaned_up)))

# this applies square root to every item in my_cleaned_up, returning a list of square roots

# dict.fromkeys
# this generates a dictionary USING a list of keys
my_dictionary = dict.fromkeys(["a", "b", "c", "d"], 0)

print(my_dictionary)
# returns a dictionary with keys a, b, c, d

# 2D array comprehension
# this is just simple, for your 'expression' within the []
twodlist = [[x for x in range(10)] for y in range(4)]

print(twodlist)