import sys
import re

from collections import defaultdict

filename = sys.argv[1]
f = open(filename, "r")
lines = f.readlines()
freq = defaultdict(int)
for thisline in lines:
    thisline_u = thisline.lower()
    words_unified = re.findall(r'\w+', thisline_u)
    for word in words_unified:
        word_index = word.lower()
        freq[word_index] +=1
print freq
