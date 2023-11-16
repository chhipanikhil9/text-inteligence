from autocorrect import Speller

def correct_spelling(sentence):

    spell = Speller(lang='en')
    
    words = sentence.split()
    corrected_words = [spell(word) for word in words]

    corrected_sentence = ' '.join(corrected_words)

    return corrected_sentence

# input_sentence = "Ths is an exaample sentance with spellin mistakes."
# output_sentence = correct_spelling(input_sentence)
# print("Original Sentence:", input_sentence)
# print("Corrected Sentence:", output_sentence)