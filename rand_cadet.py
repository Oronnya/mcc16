# random cadet number picker
import random

all_cadets = range(848, 900)

excluded = [849, 850, 851, 857, 899]

current = [x for x in all_cadets if x not in excluded]

print(random.choice(current))
