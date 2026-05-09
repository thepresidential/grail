# dictionaries are sortof hard but not that hard to wrap your head around
# these are extremely useful when required
# just imagine it as something that stores a collection of variables
# and you can reference them by calling that object

dictionary = {
    "a":"word",
    "b":"third",
    "c":"occurred",
    "d":["be","the","key"],
    "nested":{
        "thisword":"isaword",
        "id":0,
        "data":9.3
    }
}

# dictionaries can have alot of keys, but you cannot have more than one occurrence of the same key
# for example, you cannot have a separate value for 'a' if 'a' already exists within it

print(dictionary["a"])
print(dictionary["d"])
print(dictionary["nested"]["thisword"])

# dictionaries can be nested, a key inside can have its value set to another dictionary

# first, how do we iterate through it however.
# dictionary.keys() returns a list of the keys. this is one way to do it
for key in dictionary.keys():
    print(key, dictionary[key])

# dictionary.items() returns a ZIPPED copy of the keys and the values.
# don't worry about what zipped means, it just means that you can iterate through two variables at once
for key, value in dictionary.items():
    print(key, value)

# dictionary comprehension isn't as hard as well
# instead of [], it is formatted like this
# { <key expression> : <value expression> for <iterator> in <list, or range, or dict.keys()> }
dictionary = {k:3 for k in dictionary}
print(dictionary)
for key, value in dictionary.items():
    print(key, value)

# there's not really any importance in showing dict specific functions? outside these few

dictionary.pop("b") # does the same thing as the list.pop

