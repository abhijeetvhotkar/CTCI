def rotation(str1, str2):
    if len(str1) == len(str2):
        return (str2 + str2).find(str1) > 0
    else:
        return False

print(rotation("waterbottle", "erbottlewat"))
print(rotation("foo", "bar"))
print(rotation("foobar", "barfoo"))
print(rotation("foo", "ofo"))
