# AI Chat Log Summarizer
# Started as part of a learning exercise to apply NLP and text analysis skills.

def parse_chat(file_path):
    #to store user and AI messages
    user_msgs = []
    ai_msgs = []

    #file opening and separating user and AI texts
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith("User:"):
                user_msgs.append(line[len("User:"):].strip())
            elif line.startswith("AI:"):
                ai_msgs.append(line[len("AI:"):].strip())
    
    return user_msgs, ai_msgs

#Tester function
if __name__ == "__main__":
    user, ai = parse_chat("chat_log.txt")
    print("User Messages:")
    print(user)
    print("AI Messages:")
    print(ai)
