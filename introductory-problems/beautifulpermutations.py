def beautiful_permutation(n):
    if n == 2 or n == 3:
        print("NO SOLUTION")
        return
    evens = list(range(2, n+1, 2))
    odds = list(range(1, n+1, 2))
    print(" ".join(map(str, evens + odds)))

n = int(input())
beautiful_permutation(n)
