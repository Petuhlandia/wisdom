import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

text = "Backgammon is one of the oldest known board games.\n" \
       "Show me this one time please."
words = []
array = []
sentences = nltk.sent_tokenize(text)
for sentence in sentences:
    words.append(nltk.word_tokenize(sentence))

def compare_stemmer_and_lemmatizer(lemmatizer, word, pos):
    array.append(lemmatizer.lemmatize(word, pos))

lemmatizer = WordNetLemmatizer()
index = -1
for sentence in words:
    index += 1
    for word in sentence:
        compare_stemmer_and_lemmatizer(lemmatizer, word, pos = wordnet.VERB)

array = [i for i in array if str(i).isalpha()]
stop_words = set(stopwords.words("english"))
words = nltk.word_tokenize(text)
without_stop_words = [word for word in array if not word in stop_words]
print(without_stop_words)

# Step 2. Design the Vocabulary
# The default token pattern removes tokens of a single character. That's why we don't have the "I" and "s" tokens in the output
count_vectorizer = CountVectorizer()

# Step 3. Create the Bag-of-Words Model
bag_of_words = count_vectorizer.fit_transform(without_stop_words)

# Show the Bag-of-Words Model as a pandas DataFrame
feature_names = count_vectorizer.get_feature_names()
print(pd.DataFrame(bag_of_words.toarray(), columns = feature_names))