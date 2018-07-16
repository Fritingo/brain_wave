import numpy as np

dataset = []

def zeroto512(filename,file_num,Demarcation_point,off_with_head):
    record_1d = []
    for record_num in range(0,file_num,1):#record_file_num
        record_name = str(filename)+'_'+str(record_num)+'.npy'#file_name
        record=np.load(record_name)#load_file
        print(record_num)
        for time_step in range(0,512,1):#0~512
            for slicestart in range(off_with_head,Demarcation_point,1):#一維去頭去尾之train
                for ch in range(0,16,1):  #channel
                    record_1d.append(record[ch][slicestart + time_step])#list
        record_1d_arr = np.asarray(record_1d)#1d_array
        print(np.shape(record_1d_arr))
        record_3d = record_1d_arr.reshape(-1, 512, 16)#3d_array
        print(np.shape(record_3d))
    dataset.append(record_3d)#append to dataset
    print(np.shape(dataset))
    del record_1d#delete old list
    return dataset_num

def mix(dataset):
    v_max = []
    v_min = []
    for i in range(0, 16, 1):#find mix,min
        v_max.append(max(np.amax(dataset[0][:, :, i]), np.amax(dataset[1][:, :, i]),np.amax(dataset[2][:, :, i])))
        v_min.append(min(np.amin(dataset[0][:, :, i]), np.amin(dataset[1][:, :, i]),np.amin(dataset[2][:, :, i])))
    print(v_max)
    print(v_min)
    for ch_num in range(0, 16):#change to 0~1
        if (v_max[ch_num] - v_min[ch_num]) == 0:
            dataset[0][:, :, ch_num] = 0
            dataset[1][:, :, ch_num] = 0
            dataset[2][:, :, ch_num] = 0
        else:
            dataset[0][:, :, ch_num] = (((dataset[0][:, :, ch_num]) - v_min[ch_num]) / (v_max[ch_num] - v_min[ch_num]))
            dataset[1][:, :, ch_num] = (((dataset[1][:, :, ch_num]) - v_min[ch_num]) / (v_max[ch_num] - v_min[ch_num]))
            dataset[2][:, :, ch_num] = (((dataset[2][:, :, ch_num]) - v_min[ch_num]) / (v_max[ch_num] - v_min[ch_num]))
    print(np.shape(dataset))




# np.save('dataset.npy', dataset_done)

#model
# coding:UTF-8
np.set_printoptions(threshold=np.inf)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import keras
from keras.models import Model
from keras.layers import Input, LSTM, Dense, Activation, Reshape
from keras.layers.convolutional import Convolution2D, Conv1D, MaxPooling2D, MaxPooling1D, AveragePooling1D
from keras.layers.core import Flatten
from keras.optimizers import SGD, Nadam, Adamax, Adadelta, Adagrad, RMSprop
from keras.callbacks import History
from keras.utils.vis_utils import plot_model

if __name__ == "__main__":
    #set parameter
    file_num = 1
    Demarcation_point = 4500
    off_with_head = 500
    dataset_num = file_num*(Demarcation_point-off_with_head)*3

    zeroto512('guitar', file_num, Demarcation_point,off_with_head)
    zeroto512('high', file_num, Demarcation_point,off_with_head)
    zeroto512('low',file_num, Demarcation_point,off_with_head)

    mix(dataset)
    dataset_done = np.concatenate((dataset[0], dataset[1], dataset[2]), axis=0)  # to 3d_array
    print(np.shape(dataset_done))
    print(np.amax(dataset_done), np.amin(dataset_done))
 # Parameters setting
    batch_size = 16
    epoch = 100
    time_step = 512
    ch_num = 16
    class_num = 3
    data_num = dataset_num
    # x = np.load('re-train.npy')
    x = dataset_done

    print(dataset_num)

    # print(tight_data.shape)
    y = np.zeros(int(dataset_num))
    # y_train[0:10500] = 0
    print(y)
    y[int(dataset_num/3):(int((dataset_num)/3)*2)] = 1
    y[(int((dataset_num)/3)*2):int(dataset_num)] = 2
    print(y)
    print(np.shape(y))

    # modify to one hot array
    y = keras.utils.to_categorical(y, class_num)
    #y_test = keras.utils.to_categorical(y_test , class_num)
    print(y)
    print(np.shape(y))
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
              validation_split=0.2,
              epochs=epoch,
              verbose=1,
              batch_size=batch_size,
              shuffle=True)

    # Evaluate
    score = model.evaluate(x, y, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    model.save('finally_ghl.h5')