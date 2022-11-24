import random
def activation(s):
    if s>=0:
        return 1
    else:
        return -1
bias = 1
sample = [[-1, -1, bias, -1],
          [-1, 1, bias, -1],
          [1, -1, bias, -1],
          [1, 1, bias, 1]]
w1 = random.randint(0, 1)
w2 = random.randint(0, 1)
print(w1,w2)
n = 0.1
ans = 0
for x1,x2,x3,y in sample:
    while ans!=y:
        s = w1*x1 + w2*x2 - x3
        ans = activation(s)
        if ans == y:
            print("Final weight values")
            print(w1, w2)
            break
        else:
            error = y - ans
            w1 = w1 + n * error * x1
            w2 = w2 + n * error * x2