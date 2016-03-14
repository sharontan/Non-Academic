from itertools import combinations

f = open('A-large-practice.in', 'r')
op = open('Large_output.txt', 'w')

first = int(f.readline())
ind_list = []
for run in range(1, first+1):
    credit = int(f.readline())
    num = f.readline()
    items = list(map(int, f.readline().split(' ')))
    for x in combinations(items, 2):
        if x[0] + x[1] == credit:
            fir = items.index(x[0]) + 1
            ind_list.append(fir)
            if x[0] == x[1]:
                r_items = items[fir:]
                snd = r_items.index(x[1])+1
                ind_list.append(snd+fir)
            else:
                ind_list.append(items.index(x[1])+1)
    op.write("Case #{}: {} {}\n".format(run, ind_list[0], ind_list[1]))
    ind_list = []
            

