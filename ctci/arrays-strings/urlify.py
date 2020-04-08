def URLify(str: str):
    a = str.strip().split(' ')
    return '%20'.join(a)


if __name__ == "__main__":
    string = 'Hello There man how does it do       '
    print(URLify(string))
