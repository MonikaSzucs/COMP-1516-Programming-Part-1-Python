# Monika Szucs

helloWorld = "Hello World!"
line = "This is my first python program!"
breaks = "\n"
fullSentence = ""

print(helloWorld)
print(line)

print(breaks)

print(helloWorld + breaks + line)

print(breaks)

def my_world():
    fullSentence = helloWorld
    fullSentence += breaks
    fullSentence += line
    print(fullSentence)

my_world()