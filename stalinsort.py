def stalinSort(x):
    m = x[0]
    for i in range(1, len(x)):
        m = max(m, x[i])
        if (m>x[i]):
            x[i] = None
