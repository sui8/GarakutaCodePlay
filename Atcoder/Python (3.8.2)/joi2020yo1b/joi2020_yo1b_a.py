N = list(map(int, input().split()))

N.sort(reverse=True)

print(N[0] + N[1])