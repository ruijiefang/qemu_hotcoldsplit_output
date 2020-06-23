

h = {}

with open("./all_deltas.txt") as fd:
    f = fd.readlines()

for line in f:
    h[line.rstrip()] = 0

for line in f:
    h[line.rstrip()] += 1

for k in h:
    print(k + " " + str(h[k]))

cutoff=5
in_range=0
overall=0
negative=0

for k in h:
    n_k = int(k)
    overall += h[k]
    if n_k <= cutoff and n_k >= -cutoff:
        in_range += h[k]
    if n_k <= 0:
        negative += h[k]

print("# statistics:")
print("# total blocks = " + str(overall))
print("# blocks with -10<=delta<=10: " + str(in_range))
print("# percentage in range: " + str(in_range / overall * 100) + "%")
print("# blocks with delta<=0 (penalized blocks): " + str(negative))
print("# percentage penalized: " + str(negative/overall * 100) + "%")
