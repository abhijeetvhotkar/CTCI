def palindrome(string):

    string = string.replace(' ', '').lower()
    p_set = set(string)
    print(p_set)
    p_dict = {ch : 0 for ch in p_set}

    for ch in string:
        p_dict[ch] += 1

    odd_count = 0
    even_count = 0

    for ch in p_set:
        if p_dict[ch] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(p_dict)
    return odd_count <= 1

print(palindrome("Hi there ereht iH"))
print(palindrome("Just passing some gibberish text to get a wrong answer"))
