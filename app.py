from flask import Flask, render_template, request, jsonify
import features.keywordExtract as ke
# import features.grammerCorrect as gc
import features.findHash as fh
import features.meaning as mn
import features.findMail as fm
import features.findNo as fn
import features.spellCheck as sc
import features.wordCorrect as wc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        text = request.form['text']
        action = request.form['action']

        if action == 'Email Extract':
            result = fm.mail_extract(text)
        elif action == 'Number Extract':
            result = fn.extract_mobile_numbers(text)
        elif action == 'Keyword Extract':
            result = ke.extract_keyword(text)
        elif action == 'Grammar Correction':
            result = wc.correct_grammar(text)
        elif action == 'Spell Check':
            result = sc.correct_spelling(text)
        elif action == 'Hash Tag':
            result = fh.extract_hashtags(text)
        elif action == 'Meaning':
            result = mn.meaning(text)         
        else:
            result = []

        return render_template('index.html', result=result,text=text)

    return render_template('index.html', result=[])

if __name__ == '__main__':
    app.run(debug=True)


# text = "He go to the store and she is go to the park."
# # wc.correct_grammar(text)

# text = "Artificial-intelligence is revolutionizing industries. Machine-learning, a subset of AI, powers many applications. Natural language processing helps machines understand human language. AI-driven chatbots enhance customer service. NLP models like GPT-3 excel in text generation"
# # ke.extract_keyword(text)

# # mn.meaning("Awake")

# text = "Please contact john.doe@example.com or support@company.com for more information, chhipanikhil9@yahoo.com."
# # fm.mail_extract(text)

# text = "Please contact +91 9876543210 or 98765-43210 for assistance. Another number is 8888888888."
# fn.extract_mobile_numbers(text)




