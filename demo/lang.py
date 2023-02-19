import math

for j in range(1000, 9999):
    g = j % 10
    s = j // 10 % 10
    b = j // 100 % 10
    q = j // 1000
    if j == math.pow(g, 4) + math.pow(s, 4) + math.pow(b, 4) + math.pow(q, 4):
        print("%d : %d %d %d %d", j, q, b, s, g)
