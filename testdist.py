from functools import lru_cache

@lru_cache(maxsize=None)

def levenshtein_distance(a, b):
    lenA = len(a)
    lenB = len(b)

    if lenA == 0:
      return lenB
    if lenB == 0:
      return lenA

    if a[0] == b[0]:
        return levenshtein_distance(a[1:], b[1:])
    l1 = levenshtein_distance(a, b[1:])
    l2 = levenshtein_distance(a[1:], b)
    l3 = levenshtein_distance(a[1:], b[1:])
    dist = 1 + min(l1, l2, l3)

    return dist

print(levenshtein_distance('kitten', 'sitting'))
