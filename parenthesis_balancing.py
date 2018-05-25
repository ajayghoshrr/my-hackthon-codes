def ParenthesBalanced(n):
    ps = set(['{' * n + '}' * n])
    for i in range(1, n):
        for a in ParenthesBalanced(i):
            for b in ParenthesBalanced(n - i):
                ps.add(a + b)
    return ps


x = (ParenthesBalanced(5))
print (','.join(list(x)))
