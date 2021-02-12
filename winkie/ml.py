# AUTOGENERATED! DO NOT EDIT! File to edit: 04_ml.ipynb (unless otherwise specified).

__all__ = ['build_timeseries', 'build_model']

# Cell
import pandas as pd

from scipy import stats
import numpy as np

def build_timeseries(df, features, timeslice_length):
    "Split the data in `df` into timeseries segments of length `timeslice_length` containing given `features`."

    segments = []
    labels = []
    # TODO: make sure if inclusive interval (+1) is save for iteration
    for i in range(0, len(df) - timeslice_length + 1, timeslice_length):
        s = []
        i_end = i + timeslice_length
        for f in features:
            s.append(df[f[0], f[1]].values[i:i_end])

        segments.append(s)

        # collect label
        dominant_label = stats.mode(df['behavior'][i:i_end])[0][0]
        labels.append(dominant_label)

    # TODO: think about how to keep the label names,
    # See https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/
    label_vector = np.asarray(pd.get_dummies(labels), dtype = np.float32)

    return np.asarray(segments).reshape(-1, timeslice_length, len(features)), label_vector

# Cell
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import GlobalMaxPooling1D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.optimizers import Adam

def build_model(train_input, train_output):
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
    cnn.compile(loss="categorical_crossentropy", optimizer=Adam(lr=0.0015), metrics=["categorical_accuracy"])
    return cnn