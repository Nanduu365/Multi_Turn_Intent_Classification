import json 
import emoji

def validate_json_file(path):
    try:
        with open(path,'r') as f:
            json.load(f)
        return True
    except json.JSONDecodeError:
        print("Give a valid json file path")
        return False

def clean_message(text):
    text = text.lower()
    text = emoji.replace_emoji(text, replace='')

    return text

def truncate_message(message,truncate = 10):
    message = message[-truncate:-1]
    return message

def text_from_json(conversation:json):
    query = ''
    for message in conversation['messages']:

        if len(message) > 10:
            message = truncate_message(message)
        
        sender = message['sender']
        text = message['text']
        text = clean_message(text)

        query += f'{sender}: {text} \n'
        #print(query)

    return query