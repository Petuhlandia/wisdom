import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

text = "Backgammon is one of the oldest known board games."
sentences = nltk.sent_tokenize(text)
for sentence in sentences:
    print(sentence)
    print()

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    print(words)
    print()

def compare_stemmer_and_lemmatizer(stemmer, lemmatizer, word, pos):
    """
    Print the results of stemmind and lemmitization using the passed stemmer, lemmatizer, word and pos (part of speech)
    """
    print("Stemmer:", stemmer.stem(word))
    print("Lemmatizer:", lemmatizer.lemmatize(word, pos))
    print()

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
for word in words:
    compare_stemmer_and_lemmatizer(stemmer, lemmatizer, word, pos = wordnet.VERB)

#print(stopwords.words("english"))

stop_words = set(stopwords.words("english"))
words = nltk.word_tokenize(text)
without_stop_words = [word for word in words if not word in stop_words]
print(without_stop_words)

stop_words = set(stopwords.words("english"))

words = nltk.word_tokenize(text)
without_stop_words = []
for word in words:
     if word not in stop_words:
         without_stop_words.append(word)

print(without_stop_words)

# sentence = "The development of snowboarding was inspired by skateboarding, sledding, surfing and skiing."
pattern = r"[^\w]"
print(re.sub(pattern, " ", text))



# Step 2. Design the Vocabulary
# The default token pattern removes tokens of a single character. That's why we don't have the "I" and "s" tokens in the output
count_vectorizer = CountVectorizer()

# Step 3. Create the Bag-of-Words Model
bag_of_words = count_vectorizer.fit_transform(without_stop_words)

# Show the Bag-of-Words Model as a pandas DataFrame
feature_names = count_vectorizer.get_feature_names()
print(pd.DataFrame(bag_of_words.toarray(), columns = feature_names))

tfidf_vectorizer = TfidfVectorizer()
values = tfidf_vectorizer.fit_transform(without_stop_words)

feature_names = tfidf_vectorizer.get_feature_names()
print(pd.DataFrame(values.toarray(), columns = feature_names))