import language_tool_python

def correct_grammar(text):
    
    tool = language_tool_python.LanguageTool('en-US')
    checktext = tool.check(text)
    # print(checktext)
    corrections = tool.check(text)
    
    if corrections:
        corrected_text = tool.correct(text)
    return corrected_text
#     print(f"Original Text: {text}")
#     print("_________________________")
#     print(f"Corrected Text: {corrected_text}")
#     print("_________________________")

# text = "He go to the store and she is go to the park."
# corrected_text = correct_grammar(text)

