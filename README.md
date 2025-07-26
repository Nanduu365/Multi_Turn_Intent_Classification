# Multi_Turn_Intent_Classification
Build a system that takes a full WhatsApp-style multi-turn conversation between a user and a business, and classifies the final intent of the customer.


## Setup and run instructions
Follow these steps after cloning the repo.
(Create a virtual environment after cloning if needed)
+ pip install -r requirements.txt
+ python main.py

### Intructions for usage
+ Give the filepath of json file as input (a sample input_sample.json file exists in the directory. It has multiple conversationas and can be used to test the performance)
+ Choose the prefered output - csv or json
+ Wait for some time and the output will be present as out.csv or out.json in the same directory as the main.py file is. (A sample out.json and out.csv is uploaded here for reference purposes.)


## Explanation of model choice
+ Model Used -- google/gemma-3-1b-it
+ For the task of intent classification and rationale generation from conversational data (WhatsApp messages between users and AI agents), I selected the Gemma 3 1B model as it has combination of performance, size, and deployment flexibility.
+ It is compact and efficient (1B parameter model)
+ Good Performance on Short-Form Conversations
+ Strong instruction following
+ It is open-source

## Sample predictions

+ Sample input conversation 1
    + {
        "conversation_id": "conv_006",
        "messages": [
          {"sender": "user", "text": "Hi, I wanted to check if I can get an appointment with Dr. Patel this week."},
          {"sender": "agent", "text": "Sure, Dr. Patel is available on Wednesday and Thursday afternoons. Which day works better for you?"},
          {"sender": "user", "text": "Thursday afternoon would be ideal."},
          {"sender": "agent", "text": "Got it. I've booked you for Thursday at 2 PM. You'll receive a confirmation shortly."}
        ]
      },
+ Sample output 1
    + conversation_id,predicted_intent,rationale 
      conv_006,Book Appointment,The user is requesting an appointment with Dr. Patel.  {csv format}

+ For further examples refer - input_sample.json and out.csv or out.json.


## Any limitations or edge cases
+ There is a slight chance that the model may include unexpected characheters in the response
