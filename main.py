import json
from model import get_response
from preprocessing import clean_message,truncate_message,text_from_json, validate_json_file



# Functions
def convert_to_json_schema(id,predicted_intent,rationale):
    dict_obj = {
            "conversation_id": id,
            "predicted_intent": predicted_intent,
            "rationale": rationale
        }
    return dict_obj

def convert_to_csv_schema(id,predicted_intent,rationale):
    string = f'{id},{predicted_intent},{rationale}\n'
    return string
    

def predictor(data,out_format):

    if out_format == 'json':
        final_outputs =[]

        for conversation in data:
            id = conversation['conversation_id']
            
            query = text_from_json(conversation)
            result = get_response(query)  #gives intent and rationale
            # print(result)
            predicted_intent,rationale = result.split('\n')
            # print(predicted_intent,rationale)
            
            json_obj = convert_to_json_schema(id,predicted_intent,rationale)
            final_outputs.append(json_obj)

        print(final_outputs)
    
        with open('out.json','w') as f:
            json.dump(final_outputs,f, indent = 4)
  
    
    elif out_format == 'csv':
        final_outputs = ''
        for conversation in data:
            id = conversation['conversation_id']
            
            query = text_from_json(conversation)
            result = get_response(query)  #gives intent and rationale
            # print(result)
            predicted_intent,rationale = result.split('\n')
            # print(predicted_intent,rationale)
            string = convert_to_csv_schema(id,predicted_intent,rationale)
            final_outputs+=string

        with open('out.csv','w') as f:
            f.write(f'conversation_id,predicted_intent,rationale \n{final_outputs}')





# filepath = r'C:\Users\padma\Desktop\Multi_Turn_Intent_Classification\input_sample.json'
#Take input
filepath = input("Enter the json filepath: ")
    
while not (validate_json_file(filepath)):
    filepath = input("Enter the json filepath: ")

with open(filepath,'r') as f:
    data = json.load(f)


#Ask json or csv
out_format = input('Prefered output format (json or csv): ')

while (out_format.lower() != 'json') and (out_format.lower() != 'csv'):
    out_format = input('Prefered output format (json or csv): ')

# print(data)
final_outputs = []


#Main prediction
predictor(data,out_format)











