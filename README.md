# AI Chat Log Summarizer

This is a Python command-line tool that summarizes chat logs between a user and an AI. 

The idea is to parse a `.txt` file formatted like a real conversation, extract messages, perform keyword analysis, and generate a readable summary.

## ✅ Progress Updates

**Update 1:**
The tool can now:
- Parse `.txt` chat logs
- Differentiate between messages sent by the user and the AI
- Count the total number of messages, as well as per-speaker breakdown

**Update 2:** 
Basic NLP functionality has been added:
- Uses `nltk` to extract the most common keywords in the conversation (excluding common stopwords)
- Helps identify the main topic based on keyword frequency

**Update 3**
The tool can now generate a summarized answer, ready to be provided to the user

**Update 4**
The tool summarizing ability has been improved by adding `TF-IDF` keyword extraction.

🚧 Currently under development — more features coming soon.

---

## 🧠 Learning Notes

As someone new to NLP and keyword extraction, implementing this feature was a learning milestone for me.

To perform basic keyword analysis, I used Python’s `nltk` library for:
- Tokenizing sentences into words
- Removing common stopwords like “the”, “is”, and “and”
- Counting the frequency of remaining meaningful words

A useful resource I referred to during this process:
🔗 [GeeksforGeeks – Tokenize Text using NLTK](https://www.geeksforgeeks.org/tokenize-text-using-nltk-python/)

To get it working, I had to install NLTK and download the relevant datasets using:
```bash
pip install nltk
```
Then inside Python:
```bash
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```
This helped me extract relevant keywords like python, libraries, and ai, which gave insight into what the conversation was about.

## Bonus: TF-IDF Keyword Extraction

After implementing basic keyword analysis, I wanted to experiment with more advanced techniques. Which is why I tried implementing **TF-IDF (Term Frequency–Inverse Document Frequency)** — a method that gives more weight to unique, meaningful words and reduces the impact of common ones.

This was my first exposure to vector-based keyword extraction, so I spent time researching how it works and how to apply it in Python using `scikit-learn`.

### 📚 Resources I Used

Here are some of the articles and videos that helped me understand and implement TF-IDF:

- [GeeksforGeeks – Understanding TF-IDF](https://www.geeksforgeeks.org/understanding-tf-idf-term-frequency-inverse-document-frequency/)
- [FreeCodeCamp – How to Process Textual Data using TF-IDF](https://www.freecodecamp.org/news/how-to-process-textual-data-using-tf-idf-in-python-cd2bbc0a94a3/)
- [FreeCodeCamp – How to Extract Keywords with TF-IDF and Python](https://www.freecodecamp.org/news/how-to-extract-keywords-from-text-with-tf-idf-and-pythons-scikit-learn-b2a0f3d7e667/)
- 🎥 [YouTube – NLP for Beginners: Easy TF-IDF Vectorization](https://youtu.be/R1XeaYfVo6s?si=lsMf4gmj7E9jh_x8)

### 🧪 What I Learned

- **TF-IDF** helps identify words that are not just frequent, but also uniquely important to a document.
- `TfidfVectorizer` from `scikit-learn` makes it easy to apply this technique across multiple messages.
- Unlike simple frequency, TF-IDF gives more meaningful keywords and is especially useful in cases where basic counting gives too much weight to generic words like `python`.

Implementing this felt like a big step forward in understanding how real-world NLP tools work!
