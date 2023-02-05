from keras import models  
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Activation  
from keras_visualizer import visualizer 
from keras import layers 



model1 = models.Sequential() 
#model1.add(Flatten(input_shape=(10,10)))
model1.add(Dense(32, activation='relu', use_bias=False))
model1.add(Dense(16, activation='relu', use_bias=False))
model1.add(Dense(3, activation='softmax', use_bias=False))
model1.compile(optimizer='adam',
				  loss='sparse_categorical_crossentropy',
				  metrics=['accuracy'])
model1.build(input_shape=(10,10))
model1.summary()
visualizer(model1, format='png', view=True)

