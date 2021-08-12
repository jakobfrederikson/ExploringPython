# int to float... and complex?
x = 5
print("\n------------------")
print(x)
print(complex(x))
print(float(x))
print("------------------\n")

# float to int... and complex?
y = 3.3
print("------------------")
print(y)
print(complex(y))
print(int(y))
print("------------------\n")

# print length of a string
myString = "Hello World"
print("------------------")
print(myString)
print("Hello World length = ", len(myString))
print("------------------\n")

# get characters of string from index 2 to index 4
print("------------------")
print(myString[2:5])
print("------------------\n")

# remove whitespace of a string
whiteSpace = " White space is gone!"
print("------------------")
print(whiteSpace.strip())
print("------------------\n")

# upper case all of the string
print("------------------")
print(whiteSpace.upper())
print("------------------\n")

# replacing letters in a string
river = "Mississippi"
print("------------------")
print(river.replace("s","z"))
print("------------------\n")

# python cannot combine strings and numbers
# e.g: 
# age = 36
# txt = "My name is John, I am " + age
# you gotta format em
age = 21
myTxt = "My name is Jakob, I am {}"
print("------------------")
print(myTxt.format(age))
print("------------------\n")

# you can print boolean values for weird stuff
print("------------------")
print(10 == 9)     # False (capital is important)
print(10 > 9)      # True
print(bool("abc")) # this is True for some reason, w3schools says you've just evaluated it. whatever that means
print(bool(1))     # True because value for True is 1
print(bool(0))     # False because value for False is 0
print("------------------\n")

# check for values in an object
# notes:
# python seems to use plain english as operators lol
# e.g. in, is, and, or, not etc
print("------------------")
colours = ["blue", "green"]
if "blue" in colours:
    print("No way, blue is in the colours list!")
print("------------------\n")

# append value to a list
print("------------------")
coolList = ["hi", "hello", "what"]
coolList.append("cool dude")
for x in coolList:
    print(x) # I tried this for loop first try and it actually worked
             # python is cool!
print("------------------\n")

# insert a value into a specific spot in the list
print("------------------")
coolList.insert(3, "Inserted, Epicly")
for x in coolList:
    print(x)
print("------------------\n")

# remove specific value in list
print("------------------")
coolList.remove("Inserted, Epicly")
for x in coolList:
    print(x)
print("------------------\n")