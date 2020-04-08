def sockMerchant(n, ar):
    a = []
    pairs = 0
    for i in range(n):
        if ar[i] in a:
            a.remove(ar[i])
            pairs += 1
        else:
            a.append(ar[i])
    return pairs
