n = int(input())

for k in range(1, n + 1):
    total_positions = (k * k) * (k * k - 1) // 2
    
    if k > 2:
        attacking_positions = 4 * (k - 1) * (k - 2)
        print(total_positions - attacking_positions)
    else:
        print(total_positions)
