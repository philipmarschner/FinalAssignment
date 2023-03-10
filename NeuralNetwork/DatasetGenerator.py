import cv2 as cv
import time
import splitfolders


train_images = []

# take a picture from the camera
def takePicture():
    camera = cv.VideoCapture(1)
    return_value, image = camera.read()
    cv.imwrite('image.png', image)
    del(camera)
    return image

# record a video from the camera
def recordVideo(filename):
    camera = cv.VideoCapture(2)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(filename + '.avi', fourcc, 20.0, (640, 480))
    while (camera.isOpened()):
        ret, frame = camera.read()
        if ret == True:
            out.write(frame)
            cv.imshow('frame', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    camera.release()
    out.release()
    cv.destroyAllWindows()

# record a video from the camera for a specific duration
def recordVideoForDuration(filename, duration):
    camera = cv.VideoCapture(2)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(filename + '.avi', fourcc, 20.0, (640, 480))
    start = time.time()
    while (time.time() - start) < duration:
        ret, frame = camera.read()
        if ret == True:
            out.write(frame)
            cv.imshow('frame', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

# split a video into frames
def splitVideo(filename, outputFolder):
    vidcap = cv.VideoCapture(filename)
    success, image = vidcap.read()
    count = 0
    while success:
        cv.imwrite(outputFolder + "/frame%d.jpg" % count, image)  # save frame as JPEG file
        success, image = vidcap.read()
        count += 1

def splitFolders(inputFolder, outputFolder):
    splitfolders.ratio(inputFolder, outputFolder, seed=1337, ratio=(.85, .15))  # default values


#recordVideoForDuration('USBCAM_Pose2', 120)
#splitVideo('USBCAM_Pose2.avi', 'Dataset/RAW/USBCAM_Pose2')
splitFolders('Dataset/RAW', 'Dataset/SPLIT')

