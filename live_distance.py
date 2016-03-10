# USAGE
# python distance_to_camera.py

# import the necessary packages
import numpy as np
import cv2
import imutils

frame = 0

def find_marker(stream):
	global frame
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	edged = cv2.Canny(frame, 35, 125)

	# find the contours in the edged image and keep the largest one;
	# we'll assume that this is our piece of paper in the image
	(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	c = max(cnts, key = cv2.contourArea)

	# compute the bounding box of the of the paper region and return it
	return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth

# initialize the known distance from the camera to the object, which
# in this case is 24 inches
KNOWN_DISTANCE = 24.0

# initialize the known object width, which in this case, the piece of
# paper is 12 inches wide
KNOWN_WIDTH = 12.0

# initialize the list of images that we'll be using

# load the furst image that contains an object that is KNOWN TO BE 2 feet
# from our camera, then find the paper marker in the image, and initialize
# the focal length
while True:
	stream = cv2.VideoCapture(0)
	(grabbed, frame) = stream.read()
	marker = find_marker(frame)
	focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

	# load the image, find the marker in the image, then compute the
	# distance to the marker from the camera
	
	marker = find_marker(stream)
	inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])

	# draw a bounding box around the image and display it
	box = np.int0(cv2.cv.BoxPoints(marker))
	cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
	cv2.putText(stream, "%.2fft" % (inches / 12),
		(stream.shape[1] - 200, stream.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
		2.0, (0, 255, 0), 3)
	cv2.imshow("image", stream)
	cv2.waitKey(0)

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()

# end of ball_tracking code
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()

# end of ball_tracking code

