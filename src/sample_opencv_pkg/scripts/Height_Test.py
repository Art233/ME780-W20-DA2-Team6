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
        rospy.Subscriber("/camera/depth/image_raw", Image, self.depth_callback)

        rospy.Timer(rospy.Duration(0.03), self.show_img_cb)
        rospy.loginfo("Waiting for image topics...")

    def show_img_cb(self,event):
	#Display the image
    	try:


		cv2.namedWindow("RGB_Image", cv2.WINDOW_NORMAL)
		cv2.moveWindow("RGB_Image", 25, 75)


        	# And one for the depth image
		cv2.moveWindow("Depth_Image", 950, 75)
		cv2.namedWindow("Depth_Image", cv2.WINDOW_NORMAL)



            	cv2.imshow("RGB_Image",self.frame)
		#cv2.imshow("Croped_Image",self.crop_image)
                #cv2.imshow("Thres_Image", self.thres_process_image)
		#cv2.imshow("Processed_Image",self.display_image)
        	cv2.imshow("Depth_Image",self.depth_display_image)
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

	#self.count,self.countB = self.counting(self.crop_image, self.count,self.countB) 


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
        depth_array = np.array(depth_image, dtype=np.float32)

        # Normalize the depth image to fall between 0 (black) and 1 (white)
        cv2.normalize(depth_array, depth_array, 0, 1, cv2.NORM_MINMAX)

        # Process the depth image
        self.depth_display_image = self.process_depth_image(depth_array)
	print self.depth_display_image

        # Display the result
        #cv2.imshow("Depth Image", depth_display_image)


    def counting(self, frame, count,countB):
	font = cv2.FONT_HERSHEY_COMPLEX
        r = frame[240,150,2]
        g = frame[240,150,1]
        b = frame[240,150,0]
	if b > 253:
	   count = count + 1
	   if count == 5:
	     print 'find one blue'
	     countB = countB + 1	     
	elif r < 60 and g < 60 and b < 60:
	   count = 0
	
	#print count
	#print countB
	text = str(countB)
	cv2.putText(frame,text, (100, 170), font, 1, (0,255,0),)
	return count,countB

    def process_depth_image(self, frame):
        # Just return the raw image for this demo
        #print frame[240,150]
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
