# coding:UTF-8
import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import keras
from keras.models import Model
from keras.layers import Input, Dense, LSTM, Dense, Activation, Reshape
from keras.layers.convolutional import Convolution2D, Conv1D, MaxPooling2D, MaxPooling1D, AveragePooling1D
from keras.layers.core import Flatten
from keras.optimizers import SGD, Nadam, Adamax, Adadelta, Adagrad, RMSprop
from keras.callbacks import History
from keras.utils.vis_utils import plot_model




if __name__ == "__main__":

    # Parameters setting
    batch_size = 16
    epoch = 100
    time_step = 512
    ch_num = 16
    class_num = 2

    x = np.load('brain_wave_data.npy')


    # print(tight_data.shape)
    data_num = 7880
    y = np.random.rand(data_num).round()
    y[0:3940] = 0
    y[3940:7880] = 1
    print(y)
    print(np.shape(y))


    # modify to one hot array
    y = keras.utils.to_categorical(y, class_num)
    #y_test = keras.utils.to_categorical(y_test , class_num)

    # Build model
    input = Input(shape=(time_step, ch_num,), name='Input')
    output = Conv1D(filters=32, kernel_size=7, activation='relu',
                    padding='same')(input)
    output = MaxPooling1D(pool_size=2)(output)#上一層的東西往下串放在括弧裡
    output = Conv1D(filters=64, kernel_size=5, activation='relu',
                    padding='same')(output)
    output = MaxPooling1D(pool_size=2)(output)
    output = Conv1D(filters=128, kernel_size=3, activation='relu',
                    padding='same')(output)
    output = MaxPooling1D(pool_size=2)(output)
    output = Conv1D(filters=256, kernel_size=3, activation='relu',
                    padding='same')(output)
    output = MaxPooling1D(pool_size=2)(output)
    output = Flatten()(output)
    output = Dense(100, activation='relu')(output)
    output = Dense(class_num, activation='softmax')(output)

    model = Model(input, output)
    sgd = SGD(lr=0.02, decay=1e-5, momentum=0.7, nesterov=True, clipnorm=1.)
    model.compile(optimizer=sgd, loss='categorical_crossentropy',
                  metrics=['accuracy'])
    plot_model(model, to_file='model.png', show_shapes=True)

    # Train the model
    model.fit(x, y,
              # validation_data=(x_test, y_test),
              validation_split=0.1,
              epochs=epoch,
              batch_size=batch_size,
              shuffle=True)


    # Evaluate
    score = model.evaluate(x, y, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])