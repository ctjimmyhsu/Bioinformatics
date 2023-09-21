# Variables and Some Arithmetic
a = 3
b = 5
result = a**2 + b**2
print(result)

# Strings and Lists
wordOneStartPos = 22
wordOneEndPos = 27

wordTwoStartPos = 97
wordTwoEndPos = 102

textStr = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"
print(f'{textStr[wordOneStartPos:wordOneEndPos+1]} {textStr[wordTwoStartPos:wordTwoEndPos+1]}')

# Condition loops
startPos = 100
endPos = 200
result = 0
for x in range(startPos, endPos+1):
    if x % 2 != 0:
        result += x
print(result)

# Working with files
outputFile =[]

with open('input.txt','r') as f:
    outputFile = [line for pos, line in enumerate(f.readlines()) if pos % 2 != 0]
with open('output.txt','w') as f:
    f.write(''.join([line for line in outputFile]))

# Dictionaries
txtStr = "We tried list and we tried dicts also we tried Zen"

# Generic approach
wordCountDict = {}
for word in txtStr.split(' '):
    if word in wordCountDict:
        wordCountDict[word]+=1
    else:
        wordCountDict[word] = 1

# wordCountDict = Counter(txtStr.split(' '))
for key, value in wordCountDict.items():
    print(key,value)

# Fibonacci numbers
def Fibonacci_Loop(number):
    old = 1
    new = 1
    for itr in range(number-1):
        tmpVal = new
        new = old
        old = old+tmpVal
    return new


print(Fibonacci_Loop(3))

# Rabbits and Recurrence
def Fibonacci_Loop_Pythonic(months,offsprings):
    parent = 1
    child = 1
    for itr in range(months-1):
        tmpVal = child
        child = parent
        parent = parent + (tmpVal*offsprings)
    return child

print(Fibonacci_Loop_Pythonic(5,2))