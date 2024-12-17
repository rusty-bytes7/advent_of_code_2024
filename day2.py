import numpy as np
import pandas as pd

numbers_list = []
#open file 
with open ('/Users/ericawolf/vscode/inputday2.txt') as file:
    for line in file:
        clean_line = line.strip()  #remove newline characters and whitespace
        if clean_line:
            numbers_list.append(clean_line)

safecount = 0
unsafecount = 0

#define acceptable range for numbers
acceptable = {1, 2, 3, -1, -2, -3}

#process each line in numbers_list
for item in numbers_list:
    #Convert the string of numbers into a NumPy array
    array = np.fromstring(item, dtype=int, sep=' ')

    #Calculate differences between consecutive elements
    diff = np.diff(array)

    #Check if all differences are within the range [1, 3] or [-1, -3]
    if not np.all((1 <= np.abs(diff)) & (np.abs(diff) <= 3)):
        unsafecount += 1
        continue
    #check if sequence is strictly increasing or decreasing
    is_increasing = np.all(diff > 0)
    is_decreasing = np.all(diff < 0)

    #if the sequence is increasing or decreasing, mark it as safe
    if is_increasing or is_decreasing:
        safecount += 1
    else:
        unsafecount += 1  #unsafe otherwise

# Print results
print("Safe count:", safecount)
print("Unsafe count:", unsafecount)

        
 

