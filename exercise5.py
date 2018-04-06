# Mike Quaid 19032018
# Exercise 5
# script that reads the Iris data set in
# and prints the four numerical values on each row in a nice format
# replace:
# https://docs.python.org/3/library/stdtypes.html?highlight=replace#str.replace

with open("data/iris2.csv") as y:
    for line in y: #loop through each line in the data set
        line = line.replace(',', ' ') # using string method replace "," with space
        print(line[0:16].strip()) # print elements 0 to 16 and strip out all other elements of the string
