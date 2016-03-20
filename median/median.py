import heapq
n = int(input().strip())

num_list = []
less = []
more = []
equal = []
for i in range(n):
    num = int(input().strip())
    if i == 0:
        median = num
        num_list.append(num)
    elif i < 3:
        num_list.append(num)
        num_list.sort()
        if len(num_list) % 2 == 0:
            index = len(num_list) // 2 - 1
            median = (num_list[index] + num_list[index+1]) / 2
        else:
            index = (len(num_list) // 2)
            median = num_list[index]
        if i == 2:
            less.append((-1)*num_list[1])
            less.append((-1)*num_list[0])
            more.append(num_list[2])
            heapq.heapify(less)
            heapq.heapify(more)
            nodes = 3
                
    else:
        if nodes % 2 == 0:
            heapq.heappush(less, (-1)*num)
            if (less[0] * (-1)) > more[0]:
                temp = heapq.heappop(less) * (-1)
                heapq.heappush(less, (-1) * heapq.heappop(more))
                heapq.heappush(more, temp)
            nodes += 1
            median = (-1) * less[0]
        else:
            heapq.heappush(more, num)
            if (less[0] * (-1)) > more[0]:
                temp = heapq.heappop(less) * (-1)
                heapq.heappush(less, (-1) * heapq.heappop(more))
                heapq.heappush(more, temp)
            nodes += 1
            median = ((-1) * (less[0]) + more[0]) / 2
            
    print ("{0:.1f}".format(median))

