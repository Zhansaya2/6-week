from heapq import merge

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(" ".join(str(x) for x in merge(a, b)))
