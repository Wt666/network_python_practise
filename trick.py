from collections import Counter
s1="below"
s2='elbow'

print('anagram') if Counter(s1)==Counter(s2) else print("not anagram")

decimal=int('1111',2)
print(decimal)

# def binary(n):
#     s=int(n)
#     d=int(s,2)
#     return d
# binary(1010)
qsort = lambda l: l if len(l) <= 1 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort(
    [x for x in l[1:] if x >= l[0]])

print(qsort([17, 29, 11, 97, 103, 5]))
