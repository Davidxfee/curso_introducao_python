t = int(input())
N = [0] * 1000
for i in range(1000):
    N[i] = i % t

for i in range(1000):
    print(f'N[{i}] = {N[i]}')