#Mike Quaid 15/02/18
#Exercise 3
#Collatz Conjecture (https://en.wikipedia.org/wiki/Collatz_conjecture)
#start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is #even, the next term is one half the previous term. Otherwise, the next term is 3 times the previous term plus 1. The #conjecture is that no matter what value of n, the sequence will always reach 1The conjecture is that no matter what value of nominal, the sequence will always reach 1

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
