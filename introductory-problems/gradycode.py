n = int(input())

for i in range(2 ** n):
    gray = i ^ (i >> 1)
    print(f"{gray:0{n}b}") 
