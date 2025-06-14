def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))

def generate_gray_brute(n):
    from itertools import permutations
    from itertools import product
    
    all_codes = list(map(lambda x: ''.join(x), product("01", repeat=n)))

    def backtrack(path, used):
        if len(path) == len(all_codes):
            return path
        for code in all_codes:
            if code not in used and (not path or hamming_distance(code, path[-1]) == 1):
                used.add(code)
                path.append(code)
                result = backtrack(path, used)
                if result:
                    return result
                path.pop()
                used.remove(code)
        return None

    result = backtrack([], set())
    for code in result:
        print(code)
