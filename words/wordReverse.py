f = open('B-large-practice.in','r')
op = open('B-large-output.txt', 'w')

num_cases = int(f.readline())

for run in range(1, num_cases+1):
    line = f.readline().strip().split(' ')
    i = 0
    j = len(line)-1
    output = [[None]] * len(line)
    if len(line) == 1:
        output[0] = line[0]
    else:
        while i < j:
            output[j] = line[i]
            output[i] = line[j]
            i += 1
            j -= 1
            if len(line) % 2 == 1:
                mid = int(len(line) / 2)
                output[mid] = line[mid]
    string = ' '.join(output)
    op.write("Case #{}: {}\n".format(run, string))



