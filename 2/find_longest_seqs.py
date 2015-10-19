from pyfasta import Fasta
from collections import OrderedDict
from collections import defaultdict
import sys

bio_kind = sys.argv[2]

D = defaultdict(list)
f = Fasta(sys.argv[1])
for i in f.iterkeys():
    if bio_kind in i:
        D[len(f[i])].append(f[i])
sorted_D = OrderedDict(reversed(sorted(D.items())))
cur = 0
for n in sorted_D.itervalues():
    if(cur<int(sys.argv[3])):
        for i in n:
            print i
        cur+=len(n)
    else:
        break