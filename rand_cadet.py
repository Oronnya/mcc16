# random cadet number picker
import random

all_cadets = range(848, 900)

excluded = [849, 850, 851, 857, 867, 892, 899]

current = [x for x in all_cadets if x not in excluded]

# pick right-away
print(random.choice(current))

# use_dictionary?????
nexts = []
temps = []

#http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
import operator

# dict by cadet number
d = {}

for i in range(500):
    r = random.choice(current)
    
    if r in d.keys():
        d[r] = d[r] + 1
        
    else:
        d[r] = 1

#dict.iteritems() is removed in Py 3, use .items instead
#http://stackoverflow.com/questions/13998492/iteritems-in-python
chosen = max(d.items(), key=operator.itemgetter(1))[0]   
print(chosen)
