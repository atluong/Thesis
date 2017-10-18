import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time
import logging
import copy
import keras
from keras.layers.core import Dense, Activation, Dropout, RepeatVector
from keras.layers import TimeDistributed
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras import backend as K
from keras import optimizers
from keras.optimizers import Optimizer
from keras.callbacks import CSVLogger
from numpy import arange, sin, pi, random
from optimiser import SGLD
from optimiser import pSGLD
from sklearn.metrics import mean_squared_error
from math import sqrt
from scipy import stats
from sklearn.preprocessing import scale
from sklearn import preprocessing

seed = 1337
np.random.seed(seed)

def rmse(y_true, y_pred):
        return K.sqrt(K.mean(K.square(y_pred - y_true), axis=-1)) 

def gen_wave():
    t = np.arange(0.0, 10, 0.01)
    wave1 = sin(2 * 2 * pi * t)
    noise = random.normal(0, 2, len(t))
    wave1 = wave1 + noise
    wave2 = sin(2 * pi * t)
    t_rider = arange(0.0, 0.5, 0.01)
    wave3 = sin(10 * pi * t_rider)    
    insert = int(round(0.8 * len(t)))
    wave1[insert:insert + 50] = wave1[insert:insert + 50] + wave3
    return t, wave1+wave2

def get_data(seq_len):        
    data = gen_wave()
    data = np.transpose(np.array([list(i) for i in data]))
    
    sequence_length = seq_len + 1
    result = []
        
    for index in range (int(round(len(data) / sequence_length))):
        if index == (int(round(len(data) / sequence_length)) - 1):
            back = len(data) % sequence_length + 1
            result.append(data[index*sequence_length-back : index*sequence_length-back+sequence_length])    
        else:
            result.append(data[index*sequence_length : index*sequence_length + sequence_length])

    result = np.array(result)

    split = 0.8
    row = round(split * result.shape[0])
    train = result[:int(row), :]
    np.random.shuffle(train)
    x_train = train[:, :-1, :-1]
    y_train = train[:, -1, -1]
    x_test = result[int(row):, :-1, :-1]
    y_test = result[int(row):, -1, -1]

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))  

    return [x_train, y_train, x_test, y_test]        

print('> Data Loaded. Compiling...')

def build_model(layers):    
    model = Sequential()
    model.add(LSTM(layers[2], input_shape=(layers[1], layers[0]), return_sequences=True, activation='linear'))            
    model.add(LSTM(layers[3], return_sequences=True, activation='linear'))
    model.add(TimeDistributed(Dense(1, activation='linear')))    
    model.compile(loss=rmse, optimizer='Adam')
    return model

def build_model_dropout(layers):
    model = Sequential()
    model.add(LSTM(layers[2], input_shape=(layers[1], layers[0]), return_sequences=True, activation='linear', dropout=0.2))    
    model.add(LSTM(layers[3], return_sequences=True, activation='linear', dropout=0.2))
    model.add(TimeDistributed(Dense(1, activation='linear')))
    model.compile(loss=rmse, optimizer='Adam')
    return model

def build_model_sgld(layers):
    model = Sequential()
    model.add(LSTM(layers[2], input_shape=(layers[1], layers[0]), return_sequences=True, activation='linear'))    
    model.add(LSTM(layers[3], return_sequences=True, activation='linear'))
    model.add(TimeDistributed(Dense(1, activation='linear')))
    model.compile(loss=rmse, optimizer=SGLD())
    return model

sequence_length = 10 
epochs = 200

logging.basicConfig(filename='output_variables.txt', level=logging.INFO)

print('> Loading data... ')

x_train, y_train, x_test, y_test = get_data(sequence_length)

layers = [x_train.shape[2], x_train.shape[1], 300, 150, 1]

model_base = build_model(layers)
model_dropout = build_model_dropout(layers)
model_sgld = build_model_sgld(layers)

base_logger = CSVLogger('base_log.csv', append=True, separator=',')
dropout_logger = CSVLogger('dropout_log.csv', append=True, separator=',')
sgld_logger = CSVLogger('sgld_log.csv', append=True, separator=',')

print('> Training base model... ')
start = time.time()
history_base = model_base.fit(
    x_train,
    y_train,
    batch_size=sequence_length,
    nb_epoch=epochs,
    validation_data=(x_test, y_test),
    callbacks=[base_logger],
    verbose=2)
base_time = time.time() - start
logging.info('base_time = %d', base_time)

print('> Training dropout model... ')
start = time.time()
history_dropout = model_dropout.fit(
    x_train,
    y_train,
    batch_size=sequence_length,
    nb_epoch=epochs,
    validation_data=(x_test, y_test),
    callbacks=[dropout_logger],
    verbose=2)
dropout_time = time.time() - start
logging.info('dropout_time = %d', dropout_time)

print('> Training sgld model... ')
start = time.time()
history_sgld = model_sgld.fit(
    x_train,
    y_train,
    batch_size=sequence_length,
    nb_epoch=epochs,
    validation_data=(x_test, y_test),
    callbacks=[sgld_logger],
    verbose=2)
sgld_time = time.time() - start
logging.info('mcmc_time = %d', sgld_time)

print(history_base.history.keys())
fig = plt.figure()
plt.plot(history_base.history['loss'])
plt.plot(history_base.history['val_loss'])
plt.plot(history_dropout.history['val_loss'])
plt.plot(history_sgld.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['training_loss', 'base_loss', 'dropout_loss', 'mcmc_loss']) 
fig.savefig('combined_loss.png')   
plt.show()
plt.close(fig)

fig = plt.figure()
plt.plot(history_base.history['val_loss'])
plt.plot(history_dropout.history['val_loss'])
plt.plot(history_sgld.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['base_loss', 'dropout_loss', 'mcmc_loss']) 
fig.savefig('combined_no_training_loss.png')   
plt.show()
plt.close(fig)
    
fig = plt.figure()    
plt.plot(history_base.history['val_loss'])
plt.title('base model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
fig.savefig('base_loss.png')
plt.show()
plt.close(fig)

fig = plt.figure()
plt.plot(history_dropout.history['val_loss'])
plt.title('dropout model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
fig.savefig('dropout_loss.png')
plt.show()
plt.close(fig)

fig = plt.figure()
plt.plot(history_sgld.history['val_loss'])
plt.title('mcmc model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
fig.savefig('mcmc_loss.png')
plt.show()
plt.close(fig)