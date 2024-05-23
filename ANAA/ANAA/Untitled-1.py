def max_draws(p1, p2, p3):
    S = p1 + p2 + p3
    if S % 2 != 0 or p3 > p1 + p2:
        return -1
    return (S - (p3 - p1)) // 2

t = int(input())
results = []
for _ in range(t):
    p1, p2, p3 = map(int, input().split())
    results.append(max_draws(p1, p2, p3))

for result in results:
    print(result)
