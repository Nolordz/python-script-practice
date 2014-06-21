from collections import defaultdict
from operator import itemgetter
#The two lines above
word_counts = defaultdict(int)
# the above line tells the program that every word in the file is a number
with open('bible.txt' , 'r')as f:
# line above tells the program which file to open
     for  line in f :
  # for every line in the file : do something
            line = line.split()
  # do something , we splitting the words in the
            for word in line :
      # line above ..for every word in the line do something
                word_counts[word.lower()] += 1
      #line above does: counts the words and adds them by one using +=1
word_counts = reversed(sorted(word_counts.iteritems(),key=itemgetter(1)))
""" when we count the words using we want to see the most frequent word in the document
that is why we are using reversed, other way would print the least used word in the file
when we use function 'sorted' by the value not the key"""
for word, count in word_counts:
# for every word and count we found using word_counts  do something
    print "%s: %s" % (word, count)
#code does print the 'word' and the 'counts' found in the list .


