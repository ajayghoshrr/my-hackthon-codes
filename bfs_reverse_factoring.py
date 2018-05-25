#https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/




x = list(map(int,raw_input().strip().split()))
A = list(map(int,sorted(raw_input().strip().split())))
N = x[0]
K = x[1]


def is_factor(A, N):
    s = []
    for i in A:
        if int(N) % int(i) == 0:
            s.append(i)
    if len(s) == 0:
        return -1
    else:
        return sorted(s)


def func(A, N):
    a = is_factor(A, N)
    if a == -1:
        return -1
    else:
        A = a
        i = (len(A) - 1)
        l = []
        while N > 1 and i >= 0:
            if N % A[i] == 0:
                N = N / A[i]
                l.append(A[i])
            else:
                i -= 1
        if N == 1:
            return sorted(l)
        else:
            return -1
x = func(A, N)
if x == -1:
    print -1
else:
    x.insert(0, 1)
    prod = 1
    for i in range(len(x)):
        prod = prod * x[i]
        print prod,
        
