# pip install opencv-python in terminal

import cv2

cam = cv2.VideoCapture(0) 

# reading the input using the camera 
result, image = cam.read() 

# If image will detected without any error, 
# show result 
if result: 
	cv2.imshow("test", image) 

	# saving image in local storage 
	cv2.imwrite("test.png", image) 

	# If keyboard interrupt occurs, destroy image 
	# window 
	cv2.waitKey(0) 
	cv2.destroyWindow("test") 

# If captured image is corrupted, moving to else part 
else: 
	print("No image detected. Please! try again") 


