final_outputs = 'hai,hello,123\nhai,hello,123'

with open('out.csv','w') as f:
            f.write(f'conversation_id,predicted_intent,rationale \n {final_outputs}')