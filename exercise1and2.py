#Mike Quaid 04022018
#https://en.wikipedia.org/wiki/Fibonacci_number

#This function returns the nth Fibonacci number
def fib(n):
    i=0
    j=1
    n=n-1

    while n>=0:
      i,j = j,i+j
      n=n-1
    return i
#test the function with the following value
#My name is Mike so 13 (M) and 5 (E) ,so looking for 18th Fib number which is 2,584
x=18
ans=fib(x)
print("Fibonacci number",x,"is",ans)

#My surname is Quaid
#The first letter Q is number 81
#The last letter d is number 100
#Fibonacci number 181 is 30010821454963453907530667147829489881
#The ord() function is a function in Python,that converts a character to it’s ASCII value.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  return i

name = "Quaid"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
