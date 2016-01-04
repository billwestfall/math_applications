# from http://stackoverflow.com/a/3540346/5181812

import random
import sys
import subprocess
rand_word=(random.choice(list(open('/usr/share/dict/words'))))
f1=open('./rand_stuff.txt', 'w+')
f1.write(rand_word)
