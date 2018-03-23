def one_way(str1, str2):

    # Check if str1 length is less than str2
    if (len(str1) > len(str2)):
        str1, str2 = str2, str1

    # Length difference cannot be more than 1
    difference = len(str2) - len(str1)

    if (difference > 1):
        return False

    id2 = 0
    is_one_way = False

    for id1 in range(len(str1)):

        if str1[id1] != str2[id2]:
            if not is_one_way:
                is_one_way = True
                id2 += difference
            else:
                return False
        id2 += 1

    return True

print(one_way("Pale", "Pall"))
print(one_way("Pal", "Pale"))
print(one_way("Pale", "bae"))
