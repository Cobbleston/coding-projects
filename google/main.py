f = open("input").read().splitlines()

def goodness_score(s):
    if len(s) < 2:
        return 0
    elif s[0] != s[-1]:
        return 1 + goodness_score(s[1:-1])
    else:
        return goodness_score(s[1:-1])

#print(f)

for i in range(0, int(f[0])):
    res = 0
    n_k = f[1+(i)*2]
    s = f[2+(i)*2]

    #print(n_k, s)
    
    spaz = False
    n = ""
    k = ""
    for c in n_k:
        if c == " ":
            spaz = True
        elif spaz:
            k += c
        else:
            n += c
    
    n = int(n)
    k = int(k)
    
    res = k - goodness_score(s)
    
    res = "Case #" + str(i+1) + ": " + str(res)
    
    print(res)