

#--------------------------------------Combination
from itertools import combinations
def find_comp(L):
    return [",".join(map(str, comb)) for comb in combinations(L, 2)]


for _ in xrange(input()):
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    def func(val):
        y = int(val[0])
        x = int(val[1])
        return ((x-y)**int(a[1])) * ((x+y)**int(a[1]))
    s = list(set(find_comp(b)))
    #print s
    min = -9999
    mn = []
    for i in s:
        #print i.split(',')
        x = func(sorted(i.split(',')))
        #print x
        mn.append(x)
    #print mn
    print sorted(mn)[0]
   
#---------------------------------------------------------


dict_1 = {}
ascii_value_of_a = ord('a')
def difference_with_a(value):
    return abs(ascii_value_of_a - ord(value))
list_a = []
for _ in xrange(input()):
    x1 = list(raw_input())
    x = map(difference_with_a, x1)
    sum_x =sum(x)
    #print sum_x
    list_a.append(sum_x)
    #print sum_x
    dict_1[str(x1)] = sum_x
m = list(set(list_a))
max1 = -999999
# for i in m:
#     if list_a.count(i) >=max1:
#         max1 = list_a.count(i)
#     else:
#         pass
# print max1

# prod = itertools.product(a, b)
#     #print prod
#     pairs = set()
#     for x, y in prod:
#         if x != y and (y, x) not in pairs:
#             pairs.add((x, y))
#     s = list(pairs)
#     print s


s=0
#print dict_1
for i in m:
    if list_a.count(i)>1:
        s=s+((list_a.count(i)*(list_a.count(i)-1))/2)
print s

#-----------------------------------------------------------------

#Roughwork ----optimized one

from itertools import combinations
from math import pow
def find_comp(L):
    #return [",".join(map(str, comb)) for comb in combinations(L, 2)]
    return combinations(L, 2)

for _ in xrange(input()):
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    def func(val):
        mod_a = 1000000007
        y = int(val[0])
        x = int(val[1])
        return abs((pow((x-y),int(a[1])))%mod_a * (pow((x+y),int(a[1]))%mod_a))
    s = list(set(find_comp(b)))
    #print s
    #min = -9999
    mn = []
    for i in s:
        #print i.split(',')
        try:
            x = func(sorted(i))
            mn.append(x)
        except OverflowError:
            pass
        #print x
        
    #print mn
    print int(min(mn))
