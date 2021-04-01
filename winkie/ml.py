# AUTOGENERATED! DO NOT EDIT! File to edit: 04_ml.ipynb (unless otherwise specified).

__all__ = ['build_timeseries', 'build_sliding_timeseries', 'build_model', 'build_lstm_model', 'gpus']

# Cell
import pandas as pd

from scipy import stats
import numpy as np
from tqdm.notebook import trange

def build_timeseries(df, features, timeslice_length):
    "Split the data in `df` into timeseries segments of length `timeslice_length` containing given `features`."

    segments = []
    labels = []
    for i in trange(0, len(df) - timeslice_length + 1, timeslice_length):
        s = []
        i_end = i + timeslice_length
        for f in features:
            s.append(df[f[0], f[1]].values[i:i_end])

        segments.append(s)

        # collect label
        dominant_label = stats.mode(df['behavior'][i:i_end])[0][0]
        labels.append(dominant_label)

    orderd_labels = sorted(list(set(labels))) # pd.get_dummies orders alphabetically, needed for decoding
    df_encoded_labels = pd.get_dummies(labels)
    label_vector = np.asarray(df_encoded_labels, dtype = np.float32)

    return np.asarray(segments).reshape(-1, timeslice_length, len(features)), label_vector, orderd_labels

# Cell

def build_sliding_timeseries(df, features, timeslice_length):
    "Split the data in `df` into timeseries segments of length `timeslice_length` containing given `features`."

    segments = []
    labels = []
    for i in trange(0, len(df) - timeslice_length + 1):
        s = []
        i_end = i + timeslice_length
        for f in features:
            s.append(df[f[0], f[1]].values[i:i_end])

        segments.append(s)

        # collect label
        dominant_label = stats.mode(df['behavior'][i:i_end])[0][0]
        labels.append(dominant_label)

    orderd_labels = sorted(list(set(labels))) # pd.get_dummies orders alphabetically, needed for decoding
    df_encoded_labels = pd.get_dummies(labels)
    label_vector = np.asarray(df_encoded_labels, dtype = np.float32)

    return np.asarray(segments).reshape(-1, timeslice_length, len(features)), label_vector, orderd_labels

# Cell
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalMaxPooling1D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.optimizers import Adam

gpus = tf.config.list_physical_devices('GPU')
if gpus:
    # If `set_memory_growth` is not set, we observed crashes through `CUBLAS_STATUS_ALLOC_FAILED` and similar errors.
    # While we are not really sure why the default settings lead to this problem, the pragmatic approach like
    # this seems to work and is also discussed on SO:
    # https://stackoverflow.com/questions/41117740/tensorflow-crashes-with-cublas-status-alloc-failed
    tf.config.experimental.set_memory_growth(gpus[0], True)

def build_model(train_input, train_output, lr=0.0015):
    """Compile a tensorflow model for the given input and output shapes."""
    net_in = Input(shape=(train_input.shape[1:]))
    x = Conv1D(filters=64, kernel_size=2, padding="valid")(net_in)
    x = Activation("relu")(x)
    x = BatchNormalization()(x)
    x = Conv1D(filters=128, kernel_size=3, padding="valid")(x)
    x = Activation("relu")(x)
    x = BatchNormalization()(x)
    x = Conv1D(filters=16, kernel_size=4, padding="valid")(x)
    x = Activation("relu")(x)
    x = BatchNormalization()(x)
    x = GlobalMaxPooling1D()(x)
    x = Flatten()(x)
    x = Dense(128)(x)
    x = Activation("relu")(x)
    x = Dropout(rate=0.3)(x) # freezes 30% of connections to the next layer (to prevent overfitting)
    x = Dense(64)(x)
    x = Activation("relu")(x)
    x = Dropout(rate=0.3)(x)
    x = Dense(train_output.shape[1])(x)
    output = Activation("softmax")(x)

    cnn = Model(inputs=net_in, outputs=output)
    cnn.compile(loss="categorical_crossentropy", optimizer=Adam(lr=lr), metrics=["categorical_accuracy"])
    return cnn

def build_lstm_model(train_input, train_output):
    net_in = train_input.shape[1:]
    out = len(train_output[0])
    print("Output neurons: " + str(out))

    model = Sequential()
    model.add(LSTM(120, input_shape=net_in, return_sequences=True,  dropout=0.2))
    model.add(LSTM(120, input_shape=net_in, return_sequences=True,  dropout=0.2)) # added
    #model.add(LSTM(100, input_shape=input_dim, return_sequences=True,  dropout=0.2)) # added#############################################
    model.add(LSTM(100, dropout=0.2))
    model.add(Dense(100, activation="relu"))
    #model.add(Dense(80, activation="relu")) # added#########################################################
    model.add(Dense(64, activation="relu"))
    model.add(Dense(out, activation="softmax"))

    opt = Adam(lr=0.0002, clipvalue=0.5) # lr=0.0001
    model.compile(loss='categorical_crossentropy', optimizer = opt, metrics=['categorical_accuracy'])

    return model
