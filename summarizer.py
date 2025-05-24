# AI Chat Log Summarizer
# Started as part of a learning exercise to apply NLP and text analysis skills.

def parse_chat(file_path):
    #to store user and AI messages
    user_msgs = []
    ai_msgs = []

    #file opening and separating user and AI texts
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line1 = line.strip().lower() #misses text if case is different
            if line1.startswith("user:"):
                user_msgs.append(line[len("User:"):].strip())
            elif line1.startswith("ai:"):
                ai_msgs.append(line[len("AI:"):].strip())
    
    return user_msgs, ai_msgs

#Function to keep track of number of messages for user and AI
def count_messages(user_msgs, ai_msgs):
    user_count = len(user_msgs)
    ai_count = len(ai_msgs)
    total_count = user_count + ai_count
    print(f"Total Messages: {total_count}")
    print(f"User Messages: {user_count}")
    print(f"AI Messages: {ai_count}")

#Tester function
if __name__ == "__main__":
    user, ai = parse_chat("chat_log.txt")
    #print("User Messages:")
    #print(user)
    #print("AI Messages:")
    #print(ai)
    count_messages(user, ai)