def wordSearch(wordarray, word):
    dic = makedict(wordarray)
    if word not in dic:
        return 0
    else:
        return dic[word]

def makedict(wordarray):
    d = {}
    for word in wordarray:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d

def main():
    bookText = "Hi there this is a Test Do you know what a test means? Yeah its a test"
    book = bookText.lower().split(" ")
    print(book)
    print(wordSearch(book, "a"))
    print(wordSearch(book, "test"))

main()
