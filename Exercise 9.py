
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

"""def recursive_thing(calls=1):
    # "calls" argument keeps track of recursion depth
    if keep_recursing():
        # pass a higher count to the recursive call
        recursive_thing(calls + 1)
    else:
        print calls
        return"""



error = 0.0001
iterations = 0

a = input("Please enter a number to calculate to the square root of :")
x = input("Please enter a number as starting  point:")
x = float(x +(a / x)) / 2.0
next_x = float(x+(a/x))/2.0
diff = x - next_x

while  diff >= error:
    x = next_x
    next_x = float(x+(a/x))/2.0
    diff = x - next_x
    #print str(diff)
    iterations += 1


print "The result is",next_x
print iterations













