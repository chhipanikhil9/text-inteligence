import re

def mail_extract(text):


    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails = re.findall(email_pattern, text)
    
    return emails
    
    
    # print("Mail ids in the given text:\n")
    
    
    
    # print(f'{emails}\n')

