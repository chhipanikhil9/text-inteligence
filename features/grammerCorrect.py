import requests

def grammer_correct(text):
        response = requests.post(
            "https://api.sapling.ai/api/v1/edits",
            json={
                "key": '415KX7GHFUN42K1M2K03HIJIDHS039HB',
                "text": text,
                "session_id": 'test session'
            }
        )
        resp_json = response.json()
        # print(resp_json)
        if 200 <= response.status_code < 300:
            edits = resp_json['edits']
            replaced_words = []
            change = []
            print(f"Original Text: {edits[0]['sentence']}")
            
            for edit in edits:
                change.append(edit['end'])
                replaced_words.append(edit['replacement'])
            return replaced_words
            # print("Replaced Words: ")
            # print(replaced_words)
            # print("Changes: ")
            # print(change)
        else:
            print('Error: ', resp_json)

# grammer_correct("i name is nikhil?")/


# output
{'edits': [
     {'end': 1, 'error_type': 'R:DET', 'general_error_type': 'Grammar', 'id': '694fc1b4-a0b5-578e-a11f-afa15594901c', 'replacement': 'My', 'sentence': 'i name is nikhil', 'sentence_start': 0, 'start': 0},
    {'end': 16, 'error_type': 'R:ORTH', 'general_error_type': 'Spelling', 'id': 'f41dd1ae-b852-540d-90fd-b4db8a268ead', 'replacement': 'Nikhil.', 'sentence': 'i name is nikhil', 'sentence_start': 0, 'start': 10}
]}