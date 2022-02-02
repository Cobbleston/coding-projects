def second(t):
    return t[1]


def senza_doppie(w):
    res = True
    i = 0
    while (i < len(w) and res):
        if w[i] in w[:i]+w[i+1:]:
            res = False
        i += 1
    return res

def quintetto_ok(l):
    a = ""
    for w in l:
        a += w
    if senza_doppie(a):
        return True
    else:
        return False

l = open("word_list_5").read().splitlines()

alfabeto = "abcdefghijklmnopqrstuvwxyz"
d = {}

# Calcolo le occorrenze di ogni lettera
for w in l:
    for c in alfabeto:
        for e in w:
            if e == c: d[c] = d.get(c, 0) + 1

d_view = [ (v,k) for k,v in d.items() ]
d_view.sort(reverse=True) # natively sort tuples by first element
for v,k in d_view:
    print("%s: %d" % (k,v))

#print(d)

l = [w for w in l if senza_doppie(w)]

#print(l)

l = [w for w in l if ('a' not in w)]
l = [w for w in l if ('r' not in w)]
l = [w for w in l if ('o' not in w)]
l = [w for w in l if ('s' not in w)]
l = [w for w in l if ('e' not in w)]

print(l)

l = [w for w in l if ('g' not in w)]
l = [w for w in l if ('l' not in w)]
#l = [w for w in l if ('y' not in w)]
l = [w for w in l if ('p' not in w)]
l = [w for w in l if ('h' not in w)]

print(l)

l = [w for w in l if ('c' not in w)]
l = [w for w in l if ('u' not in w)]
l = [w for w in l if ('b' not in w)]
#l = [w for w in l if ('i' not in w)]
l = [w for w in l if ('t' not in w)]

print(l)

# PHYLA
# ['glyph', 'lymph', 'nymph', 'phony', 'phyla', 'pithy', 'pushy', 'sylph']
# e: 2281
# s: 2280
# a: 1825
# r: 1445
# o: 1339
# l: 1236
# i: 1196
# t: 1181
# n: 996
# d: 912
# u: 746
# c: 710
# p: 697
# m: 601
# y: 584
# h: 581
# b: 515
# g: 496
# k: 417
# f: 413
# w: 370
# v: 244
# x: 87
# z: 72
# j: 66
# q: 40