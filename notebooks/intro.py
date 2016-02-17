'''
First, we have variables.
Variables are like containers that hold values.
Values are things like numbers, words, lists of letters, etc.
'''

# In Python, we can make a variable and give it a value pretty easily.
# If we want a variable called 'foo' and want it to have a value of 1, we do:

foo = 1

# Or if we want to make foo a decimal, we do:

foo = 1.5

# with a period in the middle.
# If we want our variable foo to be a word, we do this:

foo = 'bar'

# with single quotes around the word.
# We can also make lists of numbers or words by doing this:

foo = [1,"bar",2,"baz",3]

# with commas separating the values
# You can even make a list of other lists:

foo = [[1,2],[3,4],[5,6]]

# Our variable foo can vary.  We can turn it into any value we want at any time:

foo = 2.6
foo = "quux"
foo = [100,99,98,97,96]

'''
Whether a value is a number or a word or a list of other values is called its "type".
The type of the number 5 is "integer".  The type of 'bar' is called "string".
The type of [1,2,3,4,5] is called "list".
Depending on the type of a variable or a set of variables, we can do different things:
'''

# For example If we have two numbers, we can add them:
foo = 10.0
bar = 5.0
baz = foo + bar     # baz equals 10.0

# Or we can subtract them:
baz = foo - bar     # baz equals 5.0

# Or multiply them:
baz = foo * bar     # baz equals 50.0

# Or divide them
baz = foo / bar     # baz equals 2.0

# We can also add two strings together:
foo = 'bar'
baz = 'qux'
norf = foo + baz    # norf equals 'barqux'

# We can also add two lists together:
foo = [1,2,3]
bar = ['foo', 'baz', 'qux']
baz = foo + bar     # baz equals [1,2,3,'foo','baz','qux']

# In these examples, + and - and / are called operators.
# Operators take values and turn them into something else.


'''
Most of the time we want to do more than just add and subtract numbers.
In Python, we have a bunch of tools to help us write programs
'''

'''
First, we have things called "conditional statements".
Conditional statements tell our program to do different depending on a condition.
'''

# For example, we could do something like this:
import random
foo = random.random()   # set foo to a random number
if foo < 10:    # if foo is less than 10
    print("foo is less than 10")
else: # if not, do something else
    print("foo is greater than 10")

# Or we can check for more than 2 conditions:
foo = random.random()
if foo < 10:    # if foo is less than 10
    print("foo is less than 10")
elif foo > 10 and foo < 20:     # or if foo is between 10 and 20
    print("foo is between 10 and 20")
else:   # otherwise, do something else
    print("foo is greater than 20")

# We can even have ifs inside of ifs:
foo = random.random()
if foo < 10:
    if foo > 5:
        print("foo is between 5 and 10")

'''
Sometimes, we have a bunch of values we want to work with.
For example, we might have a list of numbers that we want to print out.
To do this, we would use something called a loop.
'''

foo = [1,2,3,4,5,6,7,8,9,10]
# we can use a "for" loop to go through each value in foo:
for val in foo:     # for each value in foo
    print(val)      # print the value

# For each cycle in this loop, val will hold a different number, and we print that number.

# We can also use a while loop, which is like a mix of a conditional and a loop:
foo = 1
while foo < 10:     # as long as x is less than 10
    foo = foo + 1   # add 1 to x
print(foo)           # in this case, x is equal to 10

# Just like ifs, we can have loops inside of loops:
foo = [[1,2],[3,4],[5,6]]   # foo is a list of lists
for l in foo:               # for each list
    for number in l:        # for each number in each list
        print(number)       # print the number


'''
Now lets come back to lists.
Lists are useful for many things, and we use them often in programming.
'''
# We can access specific item in a list using something called an index
# For example if we wanted to get the first item in a list, we'd do this:

foo = [1,2,3,4,5]
first_item = foo[0]     # counting starts at 0, not 1.  Remember this!
third_item = foo[2]

# We can also access single items in lists of lists
foo = [[1,2,3],[4,5,6],[7,8,9]]
# Let's say we want to grab the number 4, we'd want the first item of the second list:
four = foo[1][0]
# We grab the second list (item at index 1), and from that list we grab the first number (item at index 0)

# '''
# Pictures are made of of things called pixels.
# Pixels are little squares on a computer screen.
# If you look closely at your screen, you can actually see each square (try it!).
# From farther away, pixels with different colors come together to look like pictures.
# We can tell our computer what color to make each pixel.
# Hundreds of pixels go across a picture in rows, and there are hundreds of rows.
# We can represent a picture as a list of lists.
# '''
#
# # Pixels are colored by mixing red, green, and blue together to form other colors.
# # We can say how much of red green and blue we want by giving a number between 0 (no color) and 255 (maximum amount of color)
# pixel = (0,0,0)
# # If we give each color a value of 0, there will be no color at all, and the pixel will be black.
# # This type with the parentheses is called a tuple.  It's like a list but a little bit simpler.
#
# # So let's say we have a picture that is 5 pixels by 5 pixels.
# # That makes a total of 25 pixels (5 x 5).
# # We could represent the picture by making a list of 5 lists of 5 pixels:
# picture = [     # So we have a list of 5 lists
#     [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)], # Each list has 5 tuples
#     [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#     [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#     [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
#     [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
# ]
#
# # This is 25 black pixels, which is a black square
# # Lets say we wanted to turn the picture white (make all colors maximum)
# i = 0   # i is our index for each row
# for row in picture:
#     j = 0   # j is our index for pixel in a row
#     for pixel in row:
#         picture[i][j] = (255,255,255)
#         j = j + 1   # add 1 to the pixel index to move on to the next pixel
#     i = i + 1   # add 1 to the row index to move on to the next row
