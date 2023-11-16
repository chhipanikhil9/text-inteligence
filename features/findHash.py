import re

def extract_hashtags(text):

    pattern = r'#\w+'
    
    hashtags = re.findall(pattern,text)
    
    return hashtags

# Example usage:

# input_text = "This is a #sample text with #hashtags. #Python is awesome!"

# result = extract_hashtags(input_text)

# print("Hashtags:", result)












