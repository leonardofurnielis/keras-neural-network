from keras import layers
from keras import models
from keras.utils import to_categorical
import pandas as pd
import numpy as np
import pickle
import nltk
import keras

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing

nltk.download('stopwords')
nltk.download('punkt')

stop_words = stopwords.words('english')
porter_stemmer = PorterStemmer()

df = pd.read_csv('../datasets/imdb-dataset.csv', delimiter=',')
df = df.head(30000)

def identify_tokens(row):
    """Identify tokens in a row
    Args:
        row (list): row of dataframe
    
    Returns:
        list: text splited in tokens
    """
    source = row[0]
    tokens = word_tokenize(source)
    token_words = [w for w in tokens if w.isalpha()]
    return token_words


def remove_stops(row):
    """Remove stop words from text
    Args:
        row (list): row of dataframe
    
    Returns:
        list: list of tokens without stop words
    """
    source_tokenization = row[2]
    stop = [w for w in source_tokenization if not w in stop_words]
    return (stop)


def stem_porter(row):
    """Execute steamming porter
    Args:
        row (list): row of dataframe
    
    Returns:
        list: list of tokens with steamming.
    """    
    my_list = row[2]
    stemmed_list = [porter_stemmer.stem(word) for word in my_list]
    return (stemmed_list)


def rejoin_words(row):
    """Join tokens in a single string
    Args:
        row (list): row of dataframe
    
    Returns:
        str: text of joined tokens
    """    
    my_list = row[2]
    joined_words = (" ".join(my_list))
    return joined_words


def pre_processing(df):
    """Execute text feature engineering (TFE)
    Args:
        df (dataframe): row of dataframe
    
    Returns:
        df: New df post text feature engineering (TFE)
    """    
    print('Tokenization')
    df['text1'] = df.apply(identify_tokens, axis=1)
    print('Remove stop words')
    df['text1'] = df.apply(remove_stops, axis=1)
    print('Stemming')
    df['text1'] = df.apply(stem_porter, axis=1)
    print('Rejoin words')
    df['clean_text'] = df.apply(rejoin_words, axis=1)

    return df


df = pre_processing(df)
df['clean_text'] = df['clean_text'].str.lower()

X = df['clean_text']
Y = df['sentiment']

X_train, X_test, Y_train, Y_test = train_test_split(X,
                                                    Y,
                                                    test_size=0.2,
                                                    random_state=48,
                                                    stratify=Y)

vectorizer = TfidfVectorizer(ngram_range=(2, 3),
                             sublinear_tf=True,
                             max_features=10000)

X_train_tf = vectorizer.fit_transform(X_train)
X_test_tf = vectorizer.transform(X_test)

le = preprocessing.LabelEncoder()

le.fit(list(Y_train))
Y_train_le = le.transform(list(Y_train))
Y_test_le = le.transform(list(Y_test))

num_class = Y.value_counts().shape
input_shape = X_train_tf.shape

Y_train_label_keras = to_categorical(Y_train_le)
Y_test_label_keras = to_categorical(Y_test_le)

# Creating neural network model
network = models.Sequential()

network.add(layers.Dense(2, activation='relu', input_shape=(input_shape[1], )))
network.add(layers.Dropout(0.4))

network.add(layers.Dense(5, activation='relu'))
network.add(keras.layers.Dropout(0.4))

network.add(layers.Dense(5, activation='sigmoid'))
network.add(layers.Dropout(0.4))

network.add(layers.Dense(num_class[0], activation='softmax'))

network.compile(optimizer='adamax',
                loss="binary_crossentropy",
                metrics=['accuracy'])

network.summary()

network.fit(X_train_tf.toarray(),
            Y_train_label_keras,
            verbose=1,
            epochs=50,
            validation_split=0.3)

# Export model to file
network.save('../models/sentiment_nn_model.keras')
pickle.dump(vectorizer, open('../models/text_vectorizer.pickle', 'wb'))
