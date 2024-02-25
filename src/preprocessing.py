from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pickle

import nltk

vectorizer = pickle.load(open('models/text_vectorizer.pickle', 'rb'))

nltk.download(['stopwords', 'punkt'], download_dir='./nltk_data')
nltk.data.path.append('./nltk_data')

stop_words = stopwords.words('english')
porter_stemmer = PorterStemmer()


def identify_tokens(text):
    """Identify tokens in a row
    Args:
        row (list): row of dataframe

    Returns:
        list: text splited in tokens
    """
    tokens = word_tokenize(text)
    token_words = [w for w in tokens if w.isalpha()]
    return token_words


def remove_stops(tokens):
    """Remove stop words from text
    Args:
        row (list): row of dataframe

    Returns:
        list: list of tokens without stop words
    """
    stop = [w for w in tokens if not w in stop_words]
    return (stop)


def stem_porter(tokens):
    """Execute steamming porter
    Args:
        row (list): row of dataframe

    Returns:
        list: list of tokens with steamming.
    """
    stemmed_list = [porter_stemmer.stem(word) for word in tokens]
    return (stemmed_list)


def rejoin_words(tokens):
    """Join tokens in a single string
    Args:
        row (list): row of dataframe

    Returns:
        str: text of joined tokens
    """
    joined_words = (" ".join(tokens))
    return joined_words


def pre_processing(text):
    """Execute text feature engineering (TFE)
    Args:
        df (dataframe): row of dataframe

    Returns:
        list: Text post text feature engineering (TFE)
    """
    tokens = identify_tokens(text)
    tokens = remove_stops(tokens)
    tokens = stem_porter(tokens)
    text = rejoin_words(tokens)

    text_tf = vectorizer.transform([text])

    return text_tf.toarray()
