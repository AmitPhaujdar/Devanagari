import pandas as pd
import numpy as np
from keras import layers
from keras.layers import *
from keras.utils import np_utils, print_summary
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint
import keras.backend as K
data = pd.read_csv(r"C:\Users\bikas\Downloads\Project_data.csv")
dataset = np.array(data)
np.random.shuffle(dataset)
X = dataset
Y = dataset
X = X[:, 0:1024]
Y = Y[:,1024]
X_train = X[0:70000,:]
X_train = X_train / 255
X_test = X[70000:72001,:]
X_test = X_test / 255
Y = Y.reshape(Y.shape[0],1)
Y_train = Y[0:70000,:]
Y_train = Y_train.T
Y_test = Y[70000:72001,:]
Y_test = Y_test.T

print("no.of training examples:"+ str(X_train.shape[0]))
print("no.of testing examples:"+ str(X_test.shape[0]))
print("X_train shape:"+ str(X_train.shape))
print("Y_train shape:"+ str(Y_train.shape))
print("X_test shape:"+ str(X_test.shape))
print("Y_test shape:"+ str(Y_test.shape))
image_X = 32
image_Y = 32

train_y = np_utils.to_categorical(Y_train)
test_y = np_utils.to_categorical(Y_test)
train_y = train_y.reshape(train_y.shape[1],train_y.shape[2])
test_y = test_y.reshape(test_y.shape[1],test_y.shape[2])
X_train = X_train.reshape(X_train.shape[0],image_X,image_Y,1)
X_test = X_test.reshape(X_test.shape[0],image_X,image_Y,1)
print(str(X_train.shape))
print(str(train_y.shape))

def keras_model(image_x,image_y):
    num_of_classes = 37
    model = Sequential()
    model.add(Conv2D(filters = 32, kernel_size = (5,5), input_shape=(image_x, image_y,1),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2),padding='same'))
    model.add(Conv2D(64,(5,5),activation='relu'))
    model.add(MaxPooling2D(pool_size=(5,5),strides=(5,5),padding='same'))
    model.add(Flatten())
    model.add(Dense(num_of_classes,activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    filepath = "devanagari.h5"
    checkpoint1 = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
    callbacks_list = [checkpoint1]
    return model,callbacks_list


model, callbacks_list = keras_model(image_X,image_Y)
model.fit(X_train, train_y, validation_data = (X_test, test_y), epochs = 1, batch_size = 64, callbacks = callbacks_list)
scores = model.evaluate(X_test, test_y, verbose = 0)
print("CNN Error : %2f%%" %(100-scores[1]*100))
print_summary(model)
model.save('devanagari.h5')










