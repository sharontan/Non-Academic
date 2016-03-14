from collections import defaultdict
from string import ascii_lowercase

f = open('C-large-practice.in','r')
op = open('C-large-practice.txt','w')

alpha = ascii_lowercase[:18]
alpha2 = ascii_lowercase[18:]
d = {}
num = 2
p = 3
q = 2
for i, alp in enumerate(alpha, 1):
    if i == p:
        d[alp] = str(num) * 3
        p += 3
        num += 1
    elif i == q:
        d[alp] = str(num) * 2
        q += 3
    else:
        d[alp] = str(num)

num2 = 7
a = 3
b = 2
for j, alp2 in enumerate(alpha2):
    if alp2 == 's':
        d[alp2] = str(num2) * 4
        num2 += 1
    elif alp2 == 'z':
        d[alp2] = '9999'
    elif j == a:
        d[alp2] = str(num2) * 3
        a += 3
        num2 += 1
    elif j == b:
        d[alp2] = str(num2) * 2
        b += 3
    else:
        d[alp2] = str(num2)
d[' '] = '0'

num_cases = int(f.readline())

output = []
last = -1
for run in range(1, num_cases+1):
    line = f.readline()
    for ind, word in enumerate(line):
        for letter in word:
            if letter == '\n':
                pass
            else:
                if d[letter][-1] == last:
                    output.append(' ')
                    output.append(d[letter])
                else:
                    output.append(d[letter])
                    last = output[-1][-1]

    op.write("Case #{}: {}\n".format(run, ''.join(output)))
    output = []
    
        


