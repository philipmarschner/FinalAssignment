import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import time
import tensorflow as tf
import struct
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Activation
from sklearn.utils import shuffle
import sys

def main():
	args = sys.argv[1:]
	if len(args) == 2 and args[0] == '-dataset_dir':
		dataset_dir = str(args[1])	

	## Use CPU only
	os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

	## Load MNIST dataset
	print("Loading dataset")
	train_images = []
	train_labels = []
	test_images = []
	test_labels = []

	dims = (10,10) # dimensions of images to train/test with

	for j in range(2): # train and test	
		for i in range(3): # 0 to 9
			if j == 0:
				read_folder = dataset_dir + '/Training/' + str(i) + '/'
			if j == 1:
				read_folder = dataset_dir + '/Testing/' + str(i) + '/'
			for filename in os.listdir(read_folder):
				img = cv2.imread(os.path.join(read_folder,filename),0) # read img as grayscale
				img = cv2.resize(img, dims, interpolation = cv2.INTER_AREA)	# resize img to fit dims
				if img is not None:
					if j == 0:
						train_images.append(img / 255) # normalize pixel vals to be between 0 - 1
						train_labels.append(i)
					if j == 1:
						test_images.append(img / 255)
						test_labels.append(i)

	## Convert to numpy arrays, flatten images - change dimensions from Nx10x10 to Nx100
	train_images = np.asarray(train_images).astype('float32')
	test_images = np.asarray(test_images).astype('float32')
	train_labels = np.asarray(train_labels).astype('uint8')
	test_labels = np.asarray(test_labels).astype('uint8')

	x = test_images[0]
	x = np.reshape(x, (1,100))
	print("test_image[0] label: ", test_labels[0])
	print("test_image[0] label: ", test_labels[1])

	print(list(x))
   





if __name__=="__main__":
	main()



