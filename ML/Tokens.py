import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import re
from tkinter import *
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def prepare_data(text):
    words = []
    array = []
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words.append(nltk.word_tokenize(sentence))

    def compare_stemmer_and_lemmatizer(lemmatizer, word, pos):
        array.append(lemmatizer.lemmatize(word, pos))

    lemmatizer = WordNetLemmatizer()
    for sentence in words:
        for word in sentence:
            compare_stemmer_and_lemmatizer(lemmatizer, word, pos=wordnet.VERB)

    array = [i for i in array if str(i).isalpha()]
    stop_words = set(stopwords.words("english"))
    without_stop_words = [word for word in array if not word in stop_words]

    # # Step 2. Design the Vocabulary
    # # The default token pattern removes tokens of a single character. That's why we don't have the "I" and "s" tokens in the output
    # count_vectorizer = CountVectorizer()
    #
    # # Step 3. Create the Bag-of-Words Model
    # bag_of_words = count_vectorizer.fit_transform(without_stop_words)
    #
    # # Show the Bag-of-Words Model as a pandas DataFrame
    #
    # feature_names = count_vectorizer.get_feature_names()
    # print(pd.DataFrame(bag_of_words.toarray(), columns=feature_names))
    global input_data
    if len(input_data) == 0:
        input_data = without_stop_words
    else:
        global wise_advice
        wise_advice.append(without_stop_words)

def from_array_to_0_1(array):
    f = open('words.txt', 'r', encoding='utf-8')
    array_0_1 = []
    for i in array:
        for j in re.findall(r"(?:(?<=\[.)|(?<=,\s.)).+?(?:(?=.\,\s)|(?=.\]))", f.read()):
            if str(i).lower() == str(j).lower():
                array_0_1.append(1)
            else:
                array_0_1.append(0)
    f.close()
    return array_0_1

def compare_text_and_wise_advice():
    global text
    text = text.get(1.0, END)
    prepare_data(text)
    global input_data, wise_advice

    f = open("wise advice.txt", "r", encoding='utf-8')
    for i in f:
        prepare_data(i)

    f.close()

    f = open("input_0_1.txt", "w", encoding='utf-8')
    f.write(str(from_array_to_0_1(input_data)))
    f.close()

    index = 1
    for i in wise_advice:
        f = open("wise_advice_{}.txt".format(index), "w", encoding='utf-8')
        f.write(str(from_array_to_0_1(i)))
        f.close()
        index += 1

    f_text = open('input_0_1.txt', "r", encoding='utf-8')
    text = re.findall('\d+', f_text.read())

    f_count = open('count.txt', "w", encoding='utf-8')
    f_count.close()

    result = ''
    count = 0
    for i in range(1, index):
        f = open("wise_advice_{}.txt".format(i), "r", encoding='utf-8')
        wise = re.findall('\d+', f.read())
        for j in range(len(text)):
            if int(text[j]) == int(wise[j]) and int(text[j]) != 0:
                count += 1
        f.close()

        f_count = open('count.txt', "a", encoding='utf-8')
        f_count.write("Wise advice {0} -> {1}\n".format(i, count))

        result += ("Wise advice {0} -> {1}\n".format(i, count))

        f_count.close()
        count = 0

    label.configure(text=str(result))
    f_text.close()

root = Tk()
root.title("ML program")
root.minsize(width = 500, height=600)

text = Text(width=60, height=10)
text.pack()
button = Button(text="start", width=10, command=compare_text_and_wise_advice)
button.pack()

label = Label()
label.pack()

input_data = []
wise_advice = []

root.mainloop()