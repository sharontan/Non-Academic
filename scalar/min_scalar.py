from itertools import combinations

f = open('A-large-practice.in','r')
op = open('A-large-output.txt','w')

num_cases = int(f.readline())
pdt = 0

for run in range(1, num_cases+1):
    arr_size = int(f.readline())
    arr1 = list(map(int, f.readline().strip().split(' ')))
    arr2 = list(map(int, f.readline().strip().split(' ')))
    s_arr1 = sorted(arr1)
    s_arr2 = sorted(arr2, reverse=True)
    for i in range(arr_size):
        pdt += s_arr1[i] * s_arr2[i]
        
    op.write("Case #{}: {}\n".format(run, pdt))
    pdt = 0
