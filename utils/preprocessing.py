import os
import ssl

from nltk import download
from nltk.data import path as nltkpath
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# This try-except block addresses SSL certificate verification issues.
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


# If the 'nltk_data' directory does not exist, download NLTK data to this directory.
if not os.path.isdir('./nltk_data'):
    download(['stopwords', 'punkt'], download_dir='./nltk_data')
    nltkpath.append('./nltk_data')


stop_words = stopwords.words('english')
porter_stemmer = PorterStemmer()


def tokenization(text):
    """Tokenizes the input text into a list of tokens.

    Args:
        text (str): The input text to be tokenized

    Returns:
        list: A list containing tokens extracted from the input text
    """
    tokens = word_tokenize(text)
    token_words = [w for w in tokens if w.isalpha()]
    return token_words


def remove_stop_words(tokens):
    """Remove stop words from a list of tokens

    Args:
        tokens (list): A list of tokens from which stop words will be removed

    Returns:
        list: A list of tokens with stop words removed
    """
    stop = [w for w in tokens if not w in stop_words]
    return (stop)


def stem_porter(tokens):
    """Execute Porter stemming on a list of tokens

    Args:
        row (list): A row of dataframe containing tokens

    Returns:
        list: A list of tokens after stemming
    """
    stemmed_list = [porter_stemmer.stem(word) for word in tokens]
    return (stemmed_list)


def rejoin_words(tokens):
    """Join tokens in a single string

    Args:
        tokens (list of str): List of tokens to be joined

    Returns:
        str: The text obtained by joining the tokens with spaces
    """
    joined_words = (" ".join(tokens))
    return joined_words


def word2vec_tfidf(vectorizer, text):
    """Execute word to vector transformation on input text using the vectorizer (TF-IDF Vectorizer)

    Args:
        vectorizer (object): Vectorizer object with transform method to convert text into vectors
        text (str): Input text to be transformed

    Returns:
        numpy.ndarray: Vector representation of the input text after transformation
    """

    text_vector = vectorizer.transform([text])

    return text_vector.toarray()
