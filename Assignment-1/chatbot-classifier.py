import datetime

responses = {} #dictionary to store responses with timestamps
while True:
    text = input("Enter: ") #taking input from user
    if not text.strip(): #if input is empty, continue to next iteration 
        continue    
    if text.lower() in ['exit', 'quit', 'stop']: #if user types exit or quit, break the loop
        print("Exiting the chatbot.")   
        break
    if text.endswith('?'): #if input ends with a question mark, classify as question
        kind = 'question' #classifying as question
    elif text.lower().startswith('how') or text.lower().startswith('what') or text.lower().startswith('why'): #if input starts with how, what, or why, classify as question
        kind = 'question'
    elif text.split(' ', 1)[0].lower() in ['please', 'do', 'run', 'open', 'close', 'start', 'stop', 'tell', 'show', 'give']: #if input starts with a command word, classify as command
        kind = 'command' #classifying as command
    else:
        kind = 'statement' #if input does not match any of the above, classify as statement
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #getting current timestamp
    #storing the response with timestamp and type
    responses[timestamp] = {'text': text, 'type': kind} #storing response in dictionary
    print(f"Type: {kind}") #printing the type of response

print("\nResponses:") #printing all responses with timestamps
#iterating through the responses dictionary and printing each response with its timestamp and type
for t, v in responses.items():
    print(f"[{t}] {v['type']}: {v['text']}") #formatted output of responses
