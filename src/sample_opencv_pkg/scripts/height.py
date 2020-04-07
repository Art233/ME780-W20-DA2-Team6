#!/usr/bin/env python


import rospy
import sys
import cv2
import serial
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
import numpy as np

class cvBridgeDemo():
    def __init__(self):
	self.count = 0
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
        rospy.Subscriber("/camera/depth/image_raw", Image, self.depth_callback)
        
        rospy.Timer(rospy.Duration(0.03), self.show_img_cb)
        rospy.loginfo("Waiting for image topics...")

    def show_img_cb(self,event):
    	try: 


		cv2.namedWindow("RGB_Image", cv2.WINDOW_NORMAL)
		cv2.moveWindow("RGB_Image", 25, 75)

        	# And one for the depth image
		cv2.moveWindow("Depth_Image", 950, 75)
		cv2.namedWindow("Depth_Image", cv2.WINDOW_NORMAL)


        	cv2.imshow("RGB_Image",self.frame)
        	cv2.imshow("Depth_Image",self.depth_display_image)

      		cv2.waitKey(3)
    	except:
		pass
	cv2.circle(self.frame,(240,340), 5, (0,255,0), -1)


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
        #self.display_image = self.process_image(frame)
	#len(self.display_image)
                       
    def depth_callback(self, ros_image):
        # Use cv_bridge() to convert the ROS image to OpenCV format
        try:
            # The depth image is a single-channel float32 image
            depth_image = self.bridge.imgmsg_to_cv2(ros_image, "32FC1")
        except CvBridgeError, e:
            print e
	    pass
        # Convert the depth image to a Numpy array since most cv2 functions
        # require Numpy arrays.
	#print len(depth_image)
        depth_array = np.array(depth_image, dtype=np.float32)
	#print depth_array[340,240]
	h = depth_array[340,240]
	#print h
	if h > 558:
		print "Nothing"
	elif h > 552 and h < 556:
		print "One layer found"
	elif h > 545 and h < 552:
		print "Two layer found"
	elif h > 539 and h < 543:
		print "Three layer found"
	elif h > 532 and h < 538:
		print "Four layer found"
	elif h > 525 and h < 530:
		print "Five layer found"
	elif h > 520 and h < 524:
		print "Six layer found"
	elif (h > 512 and h < 519) or h == 0:
		print "more than 7 layer found" 
        # Normalize the depth image to fall between 0 (black) and 1 (white)
        cv2.normalize(depth_array, depth_array, 0, 1, cv2.NORM_MINMAX)
        
        # Process the depth image
        self.depth_display_image = self.process_depth_image(depth_array)	
    
        # Display the result
        #cv2.imshow("Depth Image", depth_display_image)
    
    def process_depth_image(self, frame):
        # Just return the raw image for this demo
        return frame

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
    
