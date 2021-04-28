from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pickle

import nltk

vectorizer = pickle.load(open('data/model/vectorizer.pkl', 'rb'))

nltk.download(['stopwords', 'punkt'], download_dir='./nltk_data')
nltk.data.path.append('./nltk_data')

stop_words = stopwords.words('english')
porter_stemmer = PorterStemmer()


def identify_tokens(text):
    tokens = word_tokenize(text)
    token_words = [w for w in tokens if w.isalpha()]
    return token_words


def remove_stops(tokens):
    stop = [w for w in tokens if not w in stop_words]
    return (stop)


def stem_porter(tokens):
    stemmed_list = [porter_stemmer.stem(word) for word in tokens]
    return (stemmed_list)


def rejoin_words(tokens):
    joined_words = (" ".join(tokens))
    return joined_words


def pre_processing(text):

    tokens = identify_tokens(text)
    tokens = remove_stops(tokens)
    tokens = stem_porter(tokens)
    text = rejoin_words(tokens)

    text_tf = vectorizer.transform([text])

    return text_tf.toarray()
