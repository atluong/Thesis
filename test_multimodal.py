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
    
def ccc(x, y):
    covar = np.cov(x,y)*(len(x)-1)/float(len(x))
    xvar = np.var(x)*(len(x)-1)/float(len(x))  
    yvar = np.var(y)*(len(y)-1)/float(len(y))  
    lincc = (2 * covar) / ((xvar+yvar) +((np.mean(x)-np.mean(y))**2))
    return lincc

def get_data(seq_len):    
    speech_train = stats.zscore(np.loadtxt("train.csv", delimiter=','))
    appearance_train = stats.zscore(np.loadtxt("train_appearance.txt", delimiter=','))
    geometric_train = stats.zscore(np.loadtxt("train_geometric.txt", delimiter=','))
    label_train = np.loadtxt("train.txt", delimiter=',', usecols=2) 
    
    speech_dev = stats.zscore(np.loadtxt("dev.csv", delimiter=','))
    appearance_dev = stats.zscore(np.loadtxt("dev_appearance.txt", delimiter=','))
    geometric_dev = stats.zscore(np.loadtxt("dev_geometric.txt", delimiter=','))
    label_dev = np.loadtxt("dev.txt", delimiter=',', usecols=2)

    data_train = np.c_[speech_train, appearance_train, geometric_train]
    data_dev = np.c_[speech_dev, appearance_dev, geometric_dev]
        
    result_train = np.reshape(data_train, [len(data_train), 1, len(data_train[1])], order='F')
    result_dev = np.reshape(data_dev, [len(data_train), 1, len(data_train[1])], order='F')
    
    x_train = result_train
    x_dev = result_dev
    y_train = label_train
    y_dev = label_dev

    return [x_train, y_train, x_dev, y_dev]

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

logging.basicConfig(filename='out_variables.txt', level=logging.INFO)

print('> Loading data... ')
x_train, y_train, x_dev, y_dev = get_data(sequence_length)
print('> Data Loaded. Compiling...')

layers = [x_train.shape[2], x_train.shape[1], 300, 150, 1]

y_train = np.reshape(y_train, [len(y_train), 1, 1])
y_dev = np.reshape(y_dev, [len(y_dev), 1, 1])

model_base = build_model(layers)
model_dropout = build_model_dropout(layers)
model_sgld = build_model_sgld(layers)

base_logger = CSVLogger('base_loss.csv', append=True, separator=',')
dropout_logger = CSVLogger('dropout_loss.csv', append=True, separator=',')
sgld_logger = CSVLogger('sgld_loss.csv', append=True, separator=',')

print('> Training base model... ')
start = time.time()
history_base = model_base.fit(
    x_train,
    y_train,
    batch_size=sequence_length,
    nb_epoch=epochs,
    validation_data=(x_dev, y_dev),
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
    validation_data=(x_dev, y_dev),
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
    validation_data=(x_dev, y_dev),
    callbacks=[sgld_logger],
    verbose=2)
sgld_time = time.time() - start
logging.info('sgld_time = %d', sgld_time)

y_dev = np.reshape(y_dev, [len(y_dev)])

pred_base = model_base.predict(x_dev, batch_size=sequence_length, verbose=2)
pred_dropout = model_dropout.predict(x_dev, batch_size=sequence_length, verbose=2)
pred_sgld = model_sgld.predict(x_dev, batch_size=sequence_length, verbose=2)

pred_base = np.reshape(pred_base, [len(pred_base)])
pred_dropout = np.reshape(pred_dropout, [len(pred_dropout)])
pred_sgld = np.reshape(pred_sgld, [len(pred_sgld)])

err_base = sqrt(mean_squared_error(y_dev, pred_base))
ccc_base = ccc(y_dev, pred_base)[0,1]
logging.info("Base rmse = {}".format(err_base))
logging.info("Base ccc = {}",format(ccc_base))

err_dropout = sqrt(mean_squared_error(y_dev, pred_dropout))
ccc_dropout = ccc(y_dev, pred_dropout)[0,1]
logging.info("Dropout rmse = {}".format(err_dropout))
logging.info("Dropout ccc = {}".format(ccc_dropout))

err_sgld = sqrt(mean_squared_error(y_dev, pred_sgld))
ccc_sgld = ccc(y_dev, pred_sgld)[0,1]
logging.info("Sgld rmse = {}".format(err_sgld))
logging.info("Sgld ccc = {}".format(ccc_sgld))