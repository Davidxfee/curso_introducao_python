v = int(input())
N = [0] * 10
N[0] = v

for i in range(1, 10):
    N[i] = 2 * N[i - 1]
    
for i in range(10):
    print(f'N[{i}] = {N[i]}')