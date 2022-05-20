import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
 
def predict(voltage,current,temp):

    x_train=preprocessing.normalize(pd.read_csv(r'https://raw.githubusercontent.com/atharvakunte/SOC-estimation-data/main/Train/trainx.csv'))
    y_train=pd.read_csv(r'https://raw.githubusercontent.com/atharvakunte/SOC-estimation-data/main/Train/trainy.csv')
    x_test=preprocessing.normalize(pd.read_csv(r'https://raw.githubusercontent.com/atharvakunte/SOC-estimation-data/main/Test/testx.csv'))
    y_test=pd.read_csv(r'https://raw.githubusercontent.com/atharvakunte/SOC-estimation-data/main/Test/testy.csv')

    input_params=preprocessing.normalize([[voltage,current,temp]])
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(3, activation='linear'),
        tf.keras.layers.Dense(100, activation='relu'),
        tf.keras.layers.Dense(100, activation='relu'),
        tf.keras.layers.Dense(100, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    optimizer =  tf.keras.optimizers.Adam(
        learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07, amsgrad=False,
        name='Adam')

    model.compile(optimizer= optimizer,loss=tf.keras.losses.MeanSquaredError(),
              metrics=tf.keras.metrics.MeanSquaredError())

    model_save_name = 'SOC_SAVED_MODEL'
    path = F"./new/{model_save_name}"

    model.load_weights(path)

    output = model.predict(input_params)

    return output