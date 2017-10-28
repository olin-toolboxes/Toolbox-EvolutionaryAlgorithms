import random

def two_point_crossover(a, b):
    maxcrosslen = min(len(a), len(b))
    cx1 = random.randint(1, maxcrosslen)
    cx2 = random.randint(1, maxcrosslen - 1)

    anew = a[:cx1] + b[cx1:cx2] + a[cx2:]
    bnew = b[:cx1] + a[cx1:cx2] + b[cx2:]

    return (anew, bnew)

print(two_point_crossover("ABCDEF", "UVWXYZ"))
