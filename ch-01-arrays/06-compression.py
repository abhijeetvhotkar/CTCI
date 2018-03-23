def str_compress(string):
    if len(string) == 0:
        return ""

    compressed_string = []
    char_prev = string[0]
    count = 0

    for index in range(len(string)):
        char_present = string[index]
        if char_present == char_prev:
            count += 1
        else:
            compressed_string.append(char_prev)
            compressed_string.append(str(count))
            char_prev = char_present
            count = 1

    compressed_string.append(char_prev)
    compressed_string.append(str(count))

    string_compressed = ''.join(compressed_string)

    if len(string) <= len(string_compressed):
        return string
    else:
        return string_compressed


print(str_compress("aabbcc"))
print(str_compress("aabbbcdddd"))
