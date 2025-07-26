from transformers import pipeline
import torch
from prompt import PROMPT



def get_response(query):

    pipe = pipeline("text-generation", model="google/gemma-3-1b-it", device="cpu", torch_dtype=torch.bfloat16)


    messages = [
        [
            {
                "role": "system",
                "content": [{"type": "text", "text": PROMPT},]
            },
            {
                "role": "user",
                "content": [{"type": "text", "text": query},]
            },
        ],
    ]
    # mess = ['hai','tell me a story']
    output = pipe(messages, max_new_tokens=100,temperature = 0.5)
    # print(output)
    return output[0][0]['generated_text'][2]['content']

# get_response('hai')