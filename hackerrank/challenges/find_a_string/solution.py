def count_substring(string, sub_string):
    # num = 0
    # for i in range(len(string)):
    #     if string[i:i+len(sub_string)] == sub_string:
    #         num += 1
    # return num
    return len([i for i in range(len(string)) if string[i:i+len(sub_string)] == sub_string])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)