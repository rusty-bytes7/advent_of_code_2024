#day three
#need to find expressions of mul(number,number) EXACTLY (using regex here) and then actually multiply
#then add all together

import re

#input file
with open ('/Users/ericawolf/vscode/day3input.txt') as file:
    text = file.read()

#part1
matches = re.findall('mul[(]\d+,\d+[)]',text)

#extract numbers and multiply together
finalsum = 0
for match in matches:
    temp = re.findall(r'\d+', match)
    final = list(map(int, temp))
    multiple = final[0]*final[1]
    finalsum += multiple
print(finalsum)