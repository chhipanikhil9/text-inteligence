from PyDictionary import PyDictionary
import re

def extract_hashtags(text):
    dictionary = PyDictionary()
    hashtags = re.findall(r'#\w+', text)

    hashtag_meanings = []
    for hashtag in hashtags:
        word = hashtag[1:]
        meanings = dictionary.meaning(word)
        if meanings != None:
            for state in meanings:
                result_string = f"{hashtag}: {meanings[state]}"
            hashtag_meanings.append(result_string)

    return hashtag_meanings

# Example usage:
# text_with_hashtags = "Let's learn about #justice #Revenge and #save. #Programming is fun!"

# result = extract_hashtags(text_with_hashtags)

# # if result:
# for item in result:
#     print(item)
# else:
#     print("No hashtags found in the text.")
