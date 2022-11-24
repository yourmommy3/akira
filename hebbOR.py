def activation(w1,w2,w3):
    sum = w1+w2+w3
    if sum<=0:
        return -1
    else:
        return 1

if __name__ == '__main__':
    w1, w2, w3 = 0, 0, 0
    bias = 1
    sample = [[-1, -1, bias, -1],
              [-1, 1, bias, 1],
              [1, -1, bias, 1],
              [1, 1, bias, 1]]
    for x1, x2, x3, y in sample:
        w1 = w1 + x1 * y
        w2 = w2 + x2 * y
        w3 = w3 + x3 * y
        print(w1,w2,w3)
        activation(w1,w2,w3)
        print("Output:",end="")
        print(activation(w1,w2,w3))
        print("")