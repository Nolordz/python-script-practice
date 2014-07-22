
from random import choice # random will pick a random character
import string # will create string
from collections import defaultdict # from the collection module (file) imports to a class

def write_random_strings():
    with open('project_6.dat', 'w') as f: # we create a file 'w' = write, 'r' = read
        for i in range(0, 10): # We are telling the program how many lines we want
            s = ''.join([choice(string.ascii_lowercase) for i in range(0, 30)])
            #in the line above we are telling the program how long we want each line
            s += '\n' # this code adds a new line to the program (+add)(= already in the line)
            # + add = if not already there a '\n' new line.
            f.write(s) # we call the function to write the random strings

def count_characters():
    with open('project_6.dat') as f:
        for line in f:
            counts = defaultdict(int)
            line = line.rstrip()

            for char in line:
                counts[char] += 1

            print_results(line, counts)

def print_results(s, counts):
    print s

    import operator
    sorted_counts = reversed(sorted(counts.iteritems(), key=operator.itemgetter(1)))

    for key, value in sorted_counts:

      print key + ' => ' + str(value) + ' ',

    print

write_random_strings()
count_characters()

