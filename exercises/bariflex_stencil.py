#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

import tf2_ros
import tf2_geometry_msgs
import geometry_msgs.msg

from collections import deque

from numpy.linalg import inv

from tf.transformations import quaternion_matrix
from tf.transformations import euler_from_matrix

def color_image_callback(data):
    try:
        bridge = CvBridge()
        # Convert the ROS Image message to OpenCV2
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")

        # TODO visualize the image Hint: use cv2.imshow()
        # cv2.waitKey(1)

        # TODO: record the image. Hint: use a deque

    except CvBridgeError as e:
        rospy.logerr("CvBridge Error: {0}".format(e))

def depth_image_callback(data):
    # TODO: same as above, but for the depth image 
    # cv_image = bridge.imgmsg_to_cv2(data, "16UC1")

def main():
    
    
    # TODO: initialize the node

    # TODO: subscribe to the image and depth image topics. Use rostopic to identify the topic names 
    # TODO: image subscriber here
    # TODO: depth image subscriber here

    # tf lookup setup
    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    # initialize our data for this episode 
    data = []

    # TODO make a rospy rate 
    rate = ... 
    
    prev_pose = None
    while not rospy.is_shutdown():
        try:
            # tf lookup
            trans = tf_buffer.lookup_transform('camera_link', 'map', rospy.Time(0))
            translation = trans.transform.translation
            rotation = trans.transform.rotation

            # TODO: print the rotation and translation. what are the types? 
            # TODO: compute the 4x4 transform matrix representing the pose in the map. Hint: use quaternion_matrix. 
            # TODO: compute the relative pose between this pose and the previous pose, prev_pose 
            # TODO: record the relative pose together with the most recent depth and color image received by subscribers 

        except Exception as e:
            print("oops:", e)

        rate.sleep()

    rospy.spin()

if __name__ == '__main__':
    main()