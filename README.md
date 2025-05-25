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
