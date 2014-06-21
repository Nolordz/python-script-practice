
import datetime
import time


"""with open("C:\Users\CODING\PycharmProjects\Class Exercises\dates.txt") as future_date:
    for future_epoch in future_date:
        epoch_diff = float(future_epoch) - time.time()
        day_diff = int(epoch_diff / 86400)
        future_day = datetime.datetime.utcfromtimestamp(float(future_epoch))

        print "%s is happening in %s days" % (future_day , day_diff)"""

"""
print the number
if that number is divisible by 3, print 'fizz' instead of the number
if that number is divisible by 5, print 'buzz' instead of the number
if that number is divisible by 3 AND 5, print 'fizzbuzz' instead of the number
"""


def fizzbuzz():

    old_list = range(1, 31)

    new_list = ["fizzbuzz" if x % 3 == 0 and x % 5 == 0 else "fizz" if x % 3 == 0
                else "buzz" if x % 5 == 0 else x for x in old_list]

    return new_list

print fizzbuzz()