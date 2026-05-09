# file handling 101
# file handling starts with this object right here called open

file = open("example.txt", "r")

# two main parameters, the filename, and then the mode
# file name is easy, just the path of the file

# mode is harder to understand but here are the modes

"""
r - read
w - write [and overwrite contents of the file]
a - append [add a line to the file]

adding a '+' at the end of any of these modes makes it that it will create a new file if the file you are trying
to reference does not exist.

ones that you will need alot:

'r' - just read
'w+' - just write [ this will usually show up on 'save the games moves' questions]
'a+' - append [add a line to the file]

to remember them, just remember that it is the first letter of whatever action you want to do.
"""

"""
different modes have different functions / capabilities too.
"""

# read mode objects have one or two main functions that you should care about
# file = open("example.txt", "r")

# read the file as one giant block of text
print(file.read())

# read the file but return a list of just each line
print(file.readlines())

# EVERY FILE OBJECT NEEDS TO BE CLOSED AS WELL REGARDLESS OF MODE
file.close()

# you can skip this via using the 'with' function
# also, here are some writing functions (for both w and a modes)
with open("test.txt", "w+") as f: # we will make a variable f equal this object
    # and the mode details that we will create a new file if it does not exist

    # write a block of text
    f.write("hello world")

    # write a line
    f.writelines(["hello", "mate", "new line"])

# with automatically closes it after you exit that section

# some common things that may show up in the exam (and have shown up previously in big chus worksheets)

Moves = ["A1-B1", "B3-C3", "A3", "D3"]
with open("moves.txt", "w+") as f:
    f.writelines(Moves)