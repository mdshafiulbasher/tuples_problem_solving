# 01. Write a Python program to create a tuple
thisTuple = ("Apple", "Banana","orange")

# 02. Write a Python program to create a tuple with different data types.
differentTuple = ("apple", 65, True )
print(differentTuple)

# 03. Write a Python program to create a tuple of numbers and print one item.
numbers = (5,6,9,8,2,1,7,10)
print(numbers[5])

# 04. Write a Python program to unpack a tuple into several variables.
marks = (100, 99, 95)
(Arif , Shuvo , Himal) = marks
print(Arif)
print(Shuvo)
print(Himal)

# 05. Write a Python program to add an item to a tuple.
names = ("atik" , "mithun" , "alia")
addNames = list(names)
addNames.append("shuvo")
names = tuple(addNames)
print(names)

# 06.  Write a Python program to convert a tuple to a string
nameTuples = ('s','h','u','v','o')
nameString = ''
for item in nameTuples:
    nameString = nameString+item
print(nameString)

# 07. Write a Python program to get the 4th element from the last element of a tuple.
Rolls = (1,2,3,4,5,6,7,8,9,10)
print(Rolls[3: ])

# 08. Write a Python program to find repeated items in a tuple
subjects = ("bangla", "english", "bangla", "math", "physics", "math")
repeatedSubjects = []
singleSubject = []
for subject in subjects:
    if subject not in singleSubject:
        singleSubject.append(subject)
    else:
        repeatedSubjects.append(subject)
print(tuple(repeatedSubjects))

# 09.  Write a Python program to check whether an element exists within a tuple.
emptyTuple = ()
if len(emptyTuple) > 0:
    print("This Tuple has no Element")
else:
    print("This Tuple has no Element")

# 10. Write a Python program to convert a list to a tuple.

items = ['table', 'chair', 'computers', 'bag']
listToTuple = tuple(items)
print(listToTuple)