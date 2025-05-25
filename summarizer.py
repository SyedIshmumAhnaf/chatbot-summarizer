# AI Chat Log Summarizer
# Started as part of a learning exercise to apply NLP and text analysis skills.
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import nltk #nltk = natural language toolkit - useful for tokenizing natural language text
#example = text = "Natural language processing (NLP) is a field of computer science
#output = ['Natural', 'language', 'processing', '(', 'NLP', ')', 'is', 'a', 'field', 'of', 'computer', 'science']

try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

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

def get_keywords(messages, top_n=5):
    stop_words = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')
    words = []

    for msg in messages:
        tokens = tokenizer.tokenize(msg.lower())
        words.extend([w for w in tokens if w.isalpha() and w not in stop_words])
    
    freq = Counter(words)
    return freq.most_common(top_n)

#Tester function
if __name__ == "__main__":
    user, ai = parse_chat("chat_log.txt")
    #print("User Messages:")
    #print(user)
    #print("AI Messages:")
    #print(ai)
    count_messages(user, ai)
    all_msgs = user + ai
    keywords = get_keywords(all_msgs)
    print("\nTop Keywords (basic frequency):")
    for word, count in keywords:
        print(f"{word}: {count}")