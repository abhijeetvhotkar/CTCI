def URLify(string, length):
    list = []
    for i in range(length):
        char = string[i]
        if char == ' ':
            list.append("%20")
        else:
            list.append(char)
    return ''.join(list)


str = URLify("Mr John   Smith", 15)
print(str)
