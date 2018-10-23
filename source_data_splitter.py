d = {1:[],2:[],0:[]}


with open('sources3_6_9') as f:
    t = 18
    for n,l in enumerate(f):
        modul = n % 3

        d[modul].append([t, int(l.strip())])
        t += 2

for _ in d.values():
    print(_)


with open('source3', 'w') as f:
    for i in d[0]:
        f.write('{},{}\n'.format(*i))

with open('source6', 'w') as f:
    for i in d[1]:
        f.write('{},{}\n'.format(*i))

with open('source9', 'w') as f:
    for i in d[2]:
        f.write('{},{}\n'.format(*i))
