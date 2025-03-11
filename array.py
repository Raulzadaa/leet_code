a = []
v = []

for c in range(2):
    for b in range(2):
        d = input()
        v.append(d)
    a.append(v[:])
    v.clear()

for ind_c , c in enumerate(a):
    print(ind_c, c)

