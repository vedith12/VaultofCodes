#Sample questions 
questions = [
    "What is your name?",
    "How are you feeling today?",
    "Do you like programming? (yes/no)"
]

conversation = []  #List to store each Q&A as a dictionary

for q in questions: #Iterate through each question
    user_input = input(q + " ") # Get user input
    #Simple responses using if-else statements
    if "name" in q.lower():
        reply = f"Nice to meet you, {user_input}!"
    elif "feeling" in q.lower(): #Check if the question is about feelings
        #Check for specific feelings
        if user_input.lower() in ["good", "great", "fine", "happy"]:
            reply = "That's wonderful to hear!"
        elif user_input.lower() in ["bad", "sad", "not good"]:
            reply = "I'm sorry to hear that. Hope you feel better soon!"
        else:
            reply = "Thanks for sharing how you feel."
    elif "programming" in q.lower(): #Check if the question is about programming
        #Check for yes or no response
        if user_input.lower() == "yes":
            reply = "That's awesome! Programming is fun."
        elif user_input.lower() == "no":
            reply = "That's okay, maybe you'll like it someday!"
        else:
            reply = "Interesting answer!"
    else: #Default reply for any other question
        if user_input.strip() == "":
            reply = "You didn't answer the question." #Handling empty input
        else:
            reply = "Thank you for your response."

    #Store the question, user input, and reply
    conversation.append({
        "question": q,
        "user_input": user_input,
        "reply": reply
    })

    print("Bot:", reply) # Print a separator for clarity

# Print the conversation history
print("\nConversation Summary:")
for turn in conversation:
    print(f"Q: {turn['question']}")
    print(f"User: {turn['user_input']}")
    print(f"Bot: {turn['reply']}\n")  # Print each turn