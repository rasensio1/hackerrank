# url to Problem Spec.
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter, namedtuple
from operator import attrgetter
from itertools import groupby

def is_valid(sequence):
    counts = Counter(sequence).most_common()

    Frequency = namedtuple("frequency", ["repeats", "chars"])
    grouped = [Frequency(a,len(list(b))) for a, b in groupby(counts, lambda x: x[1])]

    if len(grouped) == 1:
        return True
    elif len(grouped) > 2:
        return False

    min_freq, max_freq = sorted(grouped, key=attrgetter("chars"))

    def one_char_off(): return min_freq.chars == 1
    def can_elim_char(): return min_freq.repeats == 1
    def freq_off_by_one(): return max_freq.repeats - min_freq.repeats in [1, -1] 

    return one_char_off() and (freq_off_by_one() or can_elim_char())

if __name__ == '__main__':
    s = input().strip()
    result = is_valid(s)
    text = ("NO", "YES")[result]
    print(text)



