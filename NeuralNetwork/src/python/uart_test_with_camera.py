import serial
import os
import random
import cv2
import numpy as np
import struct
import time
import sys
def main():
	camerasIDS = returnCameraIndexes()

	if len(camerasIDS) == 0:
		print("No camera detected")
		quit()
	elif len(camerasIDS) == 1:
		print("Only one camera detected")
		quit()
	else:
		print("Multiple cameras detected")
		if camerasIDS[0] != 0:
			#get the first camera
			camID = camerasIDS[0]
		elif camerasIDS[1] != 0:
			camID = camerasIDS[1]

	args = sys.argv[1:]
	if len(args) == 2 and args[0] == '-port':
		port = str(args[1])	


	dims = (10,10) # dimensions of images to train/test with

	#randomint = random.randrange(10)
	#read_dir = os.path.expanduser("~") + '/Downloads/MNIST_Dataset_JPG/MNIST_JPG_testing/' + str(randomint) + '/'
	#read_file = random.choice(os.listdir(read_dir)) # choose random test image
	#img = cv2.imread(os.path.join(read_dir,read_file),0) # read img as grayscale
	#print("Label: ", str(randomint), " Filename: ", read_file, " Serialport: ", port) # print test image label
	# capture image from camera
	cap = cv2.VideoCapture(camID)
	ret, img = cap.read()
	cap.release()
	# convert to grayscale
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	img = cv2.resize(img, dims, interpolation = cv2.INTER_AREA)	# resize img to fit dims
	
	cv2.imwrite("test.jpg", img) # save image to file
	# define serial connection


	img = np.asarray((img / 255)).astype('float32')
	ser = serial.Serial(port, 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

	for i in range(dims[1]):
		for j in range(dims[0]):
			values = bytearray(struct.pack("f", img[i][j])) # turn pixel values into bytearray
			#print(values)
			#time.sleep(0.01)
			ser.write(values) # send bytearray over UART

	nn_res = ""
	while "output" not in nn_res: # check if nn output received
		nn_res = ser.readline().decode('UTF-8') # decode received bytes
		#print(nn_res) # can be used to display prints from U96
	print(nn_res)

def returnCameraIndexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    print("\nIgnore the errors above, they are expected\n\n")
    return arr

	
if __name__=="__main__":
	main()
