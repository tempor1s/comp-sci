def is_permutation(s1, s2: str):
    if len(s1) != len(s2):
        return False

    a = sorted(s1)
    s1 = ' '.join(a)
    b = sorted(s2)
    s2 = ' '.join(b)

    if s1 == s2:
        return True
    return False


if __name__ == "__main__":
    s1 = 'dog'
    s2 = 'god'

    print(is_permutation(s1, s2))
