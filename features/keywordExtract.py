import csv
import string

def extract_keyword(text):
    common_words = set()

    with open('features/book.csv', 'r') as csv_file:
        reader = csv_file.read().splitlines()
        common_words.update(reader)

    allWords = text.split()

    def remove_trailing_punctuation(word):
        return word.rstrip(string.punctuation).lower()
        

    cleaned_words = [remove_trailing_punctuation(word).lower() for word in allWords]
    tempKeywords = [word for word in cleaned_words if word.lower() not in common_words]


    uniqueWords = list(set(tempKeywords))

    keywords = []
    for w in uniqueWords:
        if w not in common_words: 
            keywords.append(w)
    return keywords
    # print("Keywords of the given text: \n")
    # i=0
    # for w in keywords:
    #     print(f"Keyword {i+1} -  " + w + "\n")
    #     i+=1

extract_keyword("Artificial-intelligence is revolutionizing industries. Machine-learning, a subset of AI, powers many applications. Natural language processing helps machines understand human language. AI-driven chatbots enhance customer service. NLP models like GPT-3 excel in text generation")