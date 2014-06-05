i1 = raw_input("Please enter the first integer: ")

while not i1.isdigit():
    i1 = raw_input("Not a valid integer. Please enter the first integer: ")

i1 = int(i1)

i2 = raw_input("Please enter the second integer: ")

while i2 == '0' or not i2.isdigit():
    if i2 == '0':
        i2 = raw_input("Cannot divide by zero. Please enter the second integer: ")
    else:
        i2 = raw_input("Not valid integer. Please enter the second integer: ")

i2 = int(i2)
#This is a Test
ints_sum = i1 + i2
ints_minus = i1 - i2
ints_multi = i1 * i2
ints_divide = i1 / i2
ints_remain = i1 % i2

print "The sum of " + str(i1) + " and " + str(i2) + " is: " + str(ints_sum)
print "The difference of " + str(i1) + " and " + str(i2) + " is: " + str(ints_minus)
print "The product of" + str(i1) + " and " + str(i2) + " is: " + str(ints_multi)
print "The quotient of " + str(i1) + " and " + str(i2) + " is: " + str(ints_divide) + " with a remainder: " + \
      str(ints_remain)