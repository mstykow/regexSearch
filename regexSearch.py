#! python3
# Program opens all .txt files in current directory and searches for any line
# that matches a user-supplied regular expression.

import re, os

# Take user input and define regular expression.
# Also search for new lines for line counting purposes.
print('What would you like to search for?')
expression = input()
userRegex = re.compile(expression + '|\\n')

# Create and display a list of all .txt files in current directory.
fileFolder = os.getcwd()
fileList = []
for file in os.listdir(fileFolder):
    if file.endswith('.txt'):
        fileList.append(file)
print('Files searched: ' + ', '.join(fileList))

# Search for expression in each file and display the line number of each occurrence.
for i in fileList:
    currentFile = open(os.path.join(fileFolder, i))
    currentFileContent = currentFile.read()
    currentFile.close()
    currentMO = userRegex.findall(currentFileContent)
    if expression in currentMO:
        k = 0
        lines = []
        for j in currentMO:
            if j == expression:
                lines.append(str(k + 1))
            else:
                k = k + 1
        print(str(i) + ' contains your search string on line(s) ' + ', '.join(lines) + '.')
    else:
        print(str(i) + ' does not contain your search string.')
