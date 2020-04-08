def find_duplicates(arr):
    ht = {}
    for item in arr:
        if item in ht:
            return item
        else:
            ht[item] = 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 4, 5, 6]
    print(find_duplicates(arr))
