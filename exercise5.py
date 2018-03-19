# Mike Quaid 19032018
# Exercise 5
# script that reads the Iris data set in
# and prints the four numerical values on each row in a nice format

with open("data/iris2.csv") as x:
  for line in x:  
    print(line.split(',')[:4])
    type(line)

# print('{:2d} {:3d} {:4d} {:5d}'.format(x,x**2,x**3,x**4))
