"""
Lesson 1
Monika Szucs
"""

hello_world = "Hello World!"
line = "This is my first python program!"
breaks = "\n"
full_sentence = ""

print(hello_world)
print(line)

print(breaks)

print(hello_world + breaks + line)

print(breaks)


def my_world():
    """
    This is a function to make a sentence
    """
    print("%s%s%s" % (hello_world, breaks, line))


my_world()
