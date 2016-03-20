import sys


t = int(input().strip())
for a0 in range(t):
    R, C = input().strip().split(" ")
    R, C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
        G_t = str(input().strip())
        G.append(G_t)
    r, c = input().strip().split(" ")
    r, c = [int(r),int(c)]
    P = []
    P_i = 0
    temp = []
    for P_i in range(r):
        P_t = str(input().strip())
        P.append(P_t)
    match = 0
    matbool = False
    for m in range(len(P)):
        for row in range(len(G)):
            if P[m] in G[row]:
                match += 1
                col = G[row].index(P[m])
                a = m + 1
                b = row + 1
                while a < r and b < R:
                    if P[a] in G[b]:
                        col_mini = G[b].index(P[a])
                        if col == col_mini:
                            match += 1
                        elif col_mini > col:
                            if P[m] in G[row][col_mini:]:
                                match += 1
                    a += 1
                    b += 1
                if match == r:
                    matbool = True
                match = 0
                
    if matbool == True:
        print ("YES")
    else:
        print ("NO")

