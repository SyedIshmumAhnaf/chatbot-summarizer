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

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
except ImportError:
    TfidfVectorizer = None

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

def infer_topic(keywords):
    if not keywords:
        return "No clear topic."
    return f"The user asked mainly about {', '.join([kw for kw, _ in keywords[:2]])}."

def tfidf_keywords(messages, top_n=5):
    if not TfidfVectorizer:
        return []

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(messages)
    scores = X.sum(axis=0).A1
    terms = vectorizer.get_feature_names_out()

    ranked = sorted(zip(terms, scores), key=lambda x: x[1], reverse=True)
    return [term for term, _ in ranked[:top_n]]

def summarize(file_path):
    user_msgs, ai_msgs = parse_chat(file_path)
    all_msgs = user_msgs + ai_msgs
    total = len(all_msgs)
    keywords = get_keywords(all_msgs)
    topic = infer_topic(keywords)

    print("Summary:")
    print(f"- The conversation had {total} exchanges.")
    print(f"- {topic}")
    print(f"- Most common keywords: {', '.join([kw for kw, _ in keywords])}.")
    #print(f"- User messages: {len(user_msgs)} | AI messages: {len(ai_msgs)}")

    if TfidfVectorizer:
        tfidf = tfidf_keywords(all_msgs)
        print(f"- TF-IDF keywords: {', '.join(tfidf)}.")

    print(f"- User messages: {len(user_msgs)} | AI messages: {len(ai_msgs)}")

if __name__ == "__main__":
    file_path = "chat_log.txt"
    summarize(file_path)

'''
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
'''