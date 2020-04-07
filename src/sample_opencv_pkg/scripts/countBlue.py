#!/usr/bin/env python


import rospy
import sys
import cv2
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
import numpy as np

class cvBridgeDemo():
    def __init__(self):
	self.count = 0
	self.countB = 0
	#Don't worry, just quick setup
        self.node_name = "cv_bridge_demo"

        rospy.init_node(self.node_name)

        # What we do during shutdown
        rospy.on_shutdown(self.cleanup)

        # Create the OpenCV display window for the RGB image
        self.cv_window_name = self.node_name

        # Create the cv_bridge object
        self.bridge = CvBridge()

        # Subscribe to the camera image and depth topics and set
        # the appropriate callbacks

        rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_callback)

        rospy.Timer(rospy.Duration(0.03), self.show_img_cb)
        rospy.loginfo("Waiting for image topics...")

    def show_img_cb(self,event):
	#Display the image
    	try:

		cv2.namedWindow("RGB_Image", cv2.WINDOW_NORMAL)
		#cv2.moveWindow("RGB_Image", 25, 75)

		cv2.namedWindow("Processed_Image", cv2.WINDOW_NORMAL)
		#cv2.moveWindow("Processed_Image", 500, 75)

		cv2.namedWindow("Thres_Image", cv2.WINDOW_NORMAL)
		#cv2.moveWindow("Processed_Image", 900, 75)


            	cv2.imshow("RGB_Image",self.frame)
		cv2.imshow("Processed_Image",self.display_image)
		cv2.imshow("Thres_Image", self.thres_process_image)
            	cv2.waitKey(3)
    	except:
		pass

    def image_callback(self, ros_image):
        # Use cv_bridge() to convert the ROS image to OpenCV format
        try:
            self.frame = self.bridge.imgmsg_to_cv2(ros_image, "bgr8")
        except CvBridgeError, e:
            print e
	    pass

        # Convert the image to a Numpy array since most cv2 functions
        # require Numpy arrays.
        frame = np.array(self.frame, dtype=np.uint8)

        # Process the frame using the process_image() function
	self.crop_image = self.crop_image_process(frame)
        self.thres_process_image = self.thres_process(self.crop_image)
        self.display_image = self.process_image(self.crop_image,self.thres_process_image)
	self.count,self.countB = self.countingB(self.crop_image, self.count,self.countB) 

    def crop_image_process(self,frame):
	image = frame[0:480,200:500]
	return image

    def thres_process(self, frame):
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Blur the image
        #blur = cv2.GaussianBlur(grey, (7, 7), 0)
	blur = cv2.bilateralFilter(grey,9,75,75)

	thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]

        return thresh

    def process_image(self, frame, frame1):
        # Convert to greyscale
	r = frame[240,150,2]
        g = frame[240,150,1]
        b = frame[240,150,0]
	font = cv2.FONT_HERSHEY_COMPLEX
	_, contours, _ = cv2.findContours(frame1, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
	for cnt in contours:
		approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
		approx1 = cv2.approxPolyDP(cnt, 0.005*cv2.arcLength(cnt, True), True)
		if r < 60 and g < 60 and b < 60:
	  		cv2.putText(frame, "Nothing", (200, 170), font, 1, (0,255,0),)	
          		#print 'Object not detect'
        	else:
          		if r > 195 and r < 230:
              			if b > 196:
		  			cv2.putText(frame, "Yellow", (200, 170), font, 1, (0,255,0),)
                  			#print 'Yellow Detect'
             			elif b > 150 and b < 196:
                  			if g > 90 and g < 112:
                      			#print 'Purple Detect'
		     				cv2.putText(frame, "Purple", (200, 170), font, 1, (0,255,0),)
                  			elif g > 190 and g < 220:
                      				#print 'Orange Detect'
		      				cv2.putText(frame, "Orange", (200, 170), font, 1, (0,255,0),)
          		elif r > 253:
              		 #print 'Red detect'
	      		 cv2.putText(frame, "Red", (200, 170), font, 1, (0,255,0),)
          		elif b > 253:
              		 #print 'Blue Detect'
	      		 cv2.putText(frame, "Blue", (200, 170), font, 1, (0,255,0),)
			 cv2.drawContours(frame, [approx1], 0, (0,255,0), 5)
          		elif g > 150 and g < 180:
              			if r < 50:
              			 #print 'Green Detect'
				 cv2.putText(frame, "Green", (200, 170), font, 1, (0,255,0),)
	#cv2.circle(self.frame,(240,150), 5, (0,255,0), -1)
        return frame

    def countingB(self, frame, count,countB):
	font = cv2.FONT_HERSHEY_COMPLEX
        r = frame[240,150,2]
        g = frame[240,150,1]
        b = frame[240,150,0]
	if b > 253:
	   count = count + 1
	   if count == 2:
	     print 'found blue object'
	     countB = countB + 1	     
	elif r < 60 and g < 60 and b < 60:
	   count = 0

	text = str(countB)
	cv2.putText(frame,text, (100, 170), font, 1, (0,255,0),)
	return count,countB

    def cleanup(self):
        print "Shutting down vision node."
        cv2.destroyAllWindows()

def main(args):
    try:
        cvBridgeDemo()
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down vision node."
        cv.DestroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
