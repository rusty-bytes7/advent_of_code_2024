#this is the day 1 advent of code code

#part 1
#two lists, sort smallest to largest, then get difference between left and right
#add together differences
#import libraries
from collections import Counter
# Open the file
with open('/Users/ericawolf/vscode/input.txt', 'r') as file:
    text = file.readlines()  # Read line by line to preserve structure

# Initialize lists for left and right columns
rightlist = []
leftlist = []

# Process each line
for line in text:
    # Extract the left and right numbers based on the fixed format
    leftlist.append(line[:5].strip())   # First 5 digits (left column)
    rightlist.append(line[8:13].strip())  # Digits after 3 spaces (right column)

# Convert the lists to integers for sorting and calculations
leftlist = [int(x) for x in leftlist]
rightlist = [int(x) for x in rightlist]

# Sort the lists
leftlist.sort()
rightlist.sort()

# Get the difference between corresponding elements in the two sorted lists
result = [abs(x - y) for x, y in zip(leftlist, rightlist)]

# Calculate the sum of differences
finalsum = sum(result)

# Print the result
print("Final Sum of Differences:", finalsum)

#PART 2
#Calculate a total similarity score by adding up each number in 
#the left list after multiplying it by the number of times 
#that number appears in the right list
print(sum(x for x in rightlist if x in leftlist))
