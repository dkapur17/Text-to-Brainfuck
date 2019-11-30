# A text to Brainfuck code translator. Uses only one memory cell to print the whole message.
# Also, resets it to zero for future use.
from sys import argv

if len(argv) > 2:
    print("Usage: python3 change.py (outputFileName)")
    exit(0)

s = input("Enter text to be translated:")
# Initialize output string
outputString = ""
oldNumVal = 0
for ch in s:
    asciiVal = ord(ch)
    numVal = asciiVal - oldNumVal
    printedChar = 0
    if numVal > 0:
        for i in range(numVal):
            outputString += "+"
    elif numVal < 0:
        for i in range(-numVal):
            outputString += "-"
    outputString += "."
    oldNumVal = asciiVal
for i in range(oldNumVal):
    outputString += "-"

if len(argv) == 1:
    print(outputString)
elif len(argv) == 2:
    outputFileName = "outputs/"+argv[1]
    with open(outputFileName, "w") as f:
        f.write(outputString)
        print("Output string saved to " + outputFileName)

