# from http://stackoverflow.com/a/3540346/5181812 , this will return the random word need

import random
print(random.choice(list(open('/usr/share/dict/words'))))
