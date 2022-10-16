w = int(input())

for i in range(w):
    x = []
    x = input()
    l = len(x)
    count = 0

    if l > 10:
        for i in range(l - 2):
            count += 1

        a = x[0]
        b = x[l - 1]

        print(a, count, b, sep='')
    else:
        print(x)