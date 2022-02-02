l = open("word_list_bis").read().splitlines()
l = [w for w in l if len(w)==5]

wc = 0
for w in l:
    if len(w) == 5: wc += 1
l = sorted(l)
print("Ho ", wc, " parole nel database")

fout = open("word_list_5_bis", "w")

for w in l:
    fout.write(w + "\n")

print("finito")