"""Crete two functions , make one to handle an error,while not the other one


def handles_it(f):
    try:
        with open(f) as my_file:
            return
    except:
        print "Couldn't handle the file open."

def cant_handle_it(f):
    with open(f) as my_file:
        return

handles_it('a.txt')
 cant_handle_it('a.txt')"""
"""
Write a generator function that will return a sequence of floating point numbers

Call the function frange and have it take 3 parameters - start, stop and increment.  Assuming I pass 0, 4 and .5 as
the 3 parameters, I should see output like:

0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
"""
"""def frange(start, stop, increment):
     while start < stop:
        yield start
        start += increment

for n in frange(0, 4, 0.5):

    print n"""

def fibo():
 a = 0
 b = 1

 while True:
    yield a
    a,b = b ,a + b

x = fibo()
print x.next()
print x.next()
print x.next()
print x.next()



