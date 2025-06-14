def brute_force_min_diff(weights):
    from itertools import combinations

    total = sum(weights)
    n = len(weights)
    min_diff = float('inf')

    for i in range(n + 1):
        for subset in combinations(weights, i):
            s1 = sum(subset)
            s2 = total - s1
            min_diff = min(min_diff, abs(s1 - s2))

    return min_diff


n = int(input())
weights = list(map(int, input().split()))
print(brute_force_min_diff(weights))
