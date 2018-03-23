import sys
import os

def sort(str):
    content = []
    for value in str:
        content.append(value)
    content.sort()
    return content

def permutations(str1, str2):
    if len(str1) != len(str2):
        return print("False")
    return print(sort(str1) == sort(str2))

permutations("god", "dog")
permutations("god", "dod")
