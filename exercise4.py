#Mike Quaid 19032018
#Project Euler Problem 5 (https://projecteuler.net/problem=5)
#The smallest positive number that is evenly divisible by all of the numbers from 1 to 20

x = 1 #divisor starting at 1 
y = 2520 #2520 can be divided by 1 to 10 without a remainder,so this can be starting point for y

while x <= 20: #loop through each divisor 1 to 20
  if y % x == 0: #result must have no remainder
    x = x + 1 #increase each divisor by 1
  else:
    y=y+2520 #increase y by 2520 until all divisors result in no remainder
    x=1

print(y)
