def is_unique(string):
    seen = []
    for c in string:
        if c in seen:
            return False
        seen.append(c)
    return True


if __name__ == "__main__":
    string = 'mam'

    print(is_unique(string))
