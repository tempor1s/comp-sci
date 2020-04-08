def palindrome_perm(string):
    alphas = [x for x in string.lower() if x.isalpha()]
    hm = {}
    for c in alphas:
        hm[c] = hm.get(c, 0) + 1

    odds = 0
    for n in hm.values():
        if n % 2:
            odds += 1
    return odds <= 1


if __name__ == "__main__":
    myString = "Mr. owl ate my Metal worm"
    print(palindrome_perm(myString))
