from PyDictionary import PyDictionary


def meaning(text):
    dic = PyDictionary()

    word = dic.meaning(text)
    if(word != None):
        # print("hello")
        for state in word:
            return word[state]
    else:
            return "Meaning Not Found!"


# print(meaning("append"))
