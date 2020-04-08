# def find_unique(array):
#     ht = {}
#     for item in array:
#         ht[item] = ht.get(item, 0) + 1

#     for key, value in ht.items():
#         if value == 1:
#             return key
#     return None


# if __name__ == "__main__":
#     array = [1, 1, 3, 3, 4, 4, 6, 6, 7]
#     print(find_unique(array))

# def find_duplicate(array):
#     ht = {}
#     for item in array:
#         if ht.get(item):
#             return item
#         else:
#             ht[item] = 1
#     return None


# if __name__ == "__main__":
#     array = [1, 2, 3, 4, 4, 5, 6, 7]
#     print(find_duplicate(array))

# def two_sum(array, target):
#     d = {}
#     for item in array:
#         sum = target - item
#         if sum in d:
#             return (sum, item)
#         d[item] = item
#     return None


# if __name__ == "__main__":
#     array = [1, 2, 3, 4, 5, 6]
#     target = 5
#     print(two_sum(array, target))

# def same_elements(arr1, arr2):
#     a1 = sorted(arr1)
#     a2 = sorted(arr2)
#     return a1 == a2


# if __name__ == "__main__":
#     a1 = [1, 3, 4, 5, 3]
#     a2 = [1, 4, 3, 5, 3]
#     print(same_elements(a1, a2))

# def first_last(arrary, number):
#     for i, item in enumerate(arrary):
#         if item == number:
#             first = i
#             last = i
#             for j in range(i, len(arrary)):
#                 if arrary[j] == number:
#                     last = j
#                 else:
#                     return first, last
#             return first, last
#     return None


# if __name__ == "__main__":
#     array = [1, 2, 3, 3, 3]
#     number = 3
#     print(first_last(array, number))

# def k_largest(array, k):
#     a = sorted(array, reverse=True)
#     return a[:k]


# if __name__ == "__main__":
#     a = [1, 4, 3, 9, 4, 6, 10]
#     print(k_largest(a, 3))

def common_word(paragraph):
    ht = dict()
    array = paragraph.split(" ")
    for item in array:
        ht[item] = ht.get(item, 0) + 1

    print(ht)
    return max(ht, key=ht.get)


if __name__ == "__main__":
    string = "A cat in a hat is a feline wearing a fedora"
    print(common_word(string))
