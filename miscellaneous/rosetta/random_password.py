import random
import string

random=''.join([random.choice(string.uppercase + string.digits + string.lowercase + string.punctuation) for n in xrange(20)])
print random
