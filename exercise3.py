#Mike Quaid 15/02/18
#Exercise 3
#Collatz Conjecture (https://en.wikipedia.org/wiki/Collatz_conjecture)
#The conjecture is that no matter what value of nominal, the sequence will always reach 1

n=17 #random starting point

while n !=1:
  if n%2 == 0: 
   x =n/2 #divide by 2 if even
   print(x)
   n=x
  else:
    y = n*3+1 #multiply by three and 1 if odd
    print(y)
    n = y
