
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

error = 0.000001

#a = input("Please enter a number to calculate to the square root of :")
#old_x = input("Please enter another number as starting point:")

def newton_function(x, a):
    iterations = 0
    next_x = (x +(a / x)) / 2.0
    diff = abs(x - next_x)

    while diff > error:

        x = next_x
        next_x =( x +(a / x)) / 2
        diff = (x - next_x)
        iterations += 1

    return next_x

#print "The square root is ", new_x


import sys
import math

def test():
    sys.stdout.write("{:<3}{:<20}{:<20}{:<20}{:<20}\n".format('n', "square_root", "math.sqrt", "difference", "is difference < 0.000001?"))
    for x in range(1, 10):
        current_num = str(x)
        my_sqrt = newton_function(5, x)
        py_sqrt = math.sqrt(x)
        diff = abs(my_sqrt - py_sqrt)
        is_good = diff < 0.000001
        sys.stdout.write("{:<3}{:<20}{:<20}{:<20}{:<20}\n".format(current_num, str(my_sqrt), str(py_sqrt), str(diff), str(is_good)))

test()
#print newton_function(old_x, a)




