import cv2 as cv

name = 'pose3'

# convert image to gray
img = cv.imread(name + '.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# resize image to 10x10
resized = cv.resize(gray, (10, 10))

# save image
cv.imwrite(name + '_resized.jpg', resized)