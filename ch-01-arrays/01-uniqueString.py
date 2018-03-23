# Finding whether the string is unique

def isUnique(String):
    letters = {}
    for letter in String:
        if letter in letters:
            return print("False")
        letters[letter] = True
    return print("True")

isUnique("Hello")
isUnique("Helo")
