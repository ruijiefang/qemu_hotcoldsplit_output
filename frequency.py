

h = {}

with open("./sorted_all_deltas.txt") as fd:
    f = fd.readlines()

for line in f:
    h[line.rstrip()] = 0

for line in f:
    h[line.rstrip()] += 1

for k in h:
    print(str(h[k]) + " " + k)
