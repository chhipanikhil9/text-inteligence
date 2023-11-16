import re

def extract_mobile_numbers(text):
    mobile_pattern = r'\b[6789]\d{9}\b'

    mobile_numbers = re.findall(mobile_pattern, text)
    return mobile_numbers
    # print(mobile_numbers)

