n, m = input().split(' ')
n_val = [int(i) for i in input().split(' ')]
for _ in range(int(m)-1):
    nn_val = [int(i) for i in input().split(' ')]
    for i in range(2):
        n_val[i] = min([n_val[i], nn_val[i]])
n = int(n)
if n_val[0] > n_val[1]*6: print(n_val[1]*n)
else: print(int(n/6) * n_val[0] + min([n_val[0], (n%6)*n_val[1]]))