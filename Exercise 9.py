
from math import sqrt
from math import factorial

"""error = 0.00001
input please enter a number to calculate the square root
input please enter another number as a starting point.
create a code to calculate the square root of the first input (make sure it works)
make the Newtons formula for recursion (second input)code for to check for
print the number of the square root we are calculating
print the number of iterations (we need to create a code to count the iterations)

*2 - answer from the loop against error."""

error = 0.00001
iterations = 0

x = input("Please enter a number to calculate to the square root of :")
a = input("Please enter another number as starting point:")
next_x = x ** .5
a = float(x +(a / x)) / 2.0 - next_x
diff = a - error
print diff





sh


