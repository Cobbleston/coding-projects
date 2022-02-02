from random import random, randint

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

l = ["abets", "doubt", "gusty", "lochs", "pries", "solar", "zombi"]
l = open("word_list_5").read().splitlines()
alfabeto = "abcdefghijklmnoprstuvwxyz"

resres = []
res = []
mass = len(l)
cont = 0
while True:
    i = []
    finito = False
    while not finito:
        if len(i) == 5:
            finito = True
        else:
            n = randint(0, mass-1)
            if n not in i:
                i.append(n)
        #print("test", finito)
    #print(i)
    res = [l[i[0]], l[i[1]], l[i[2]], l[i[3]], l[i[4]]]
    #print(res)
    if quintetto_ok(res):
        resres.append(res)
        break
    cont += 1
    if cont % 1000000 == 0:
        print(cont // 1000000, "M")

print(resres)