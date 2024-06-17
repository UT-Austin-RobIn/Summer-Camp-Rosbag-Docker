#! /usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
import numpy as np


def joint_state_callback(msg):
    '''
    Prints out the header and position of the Joint State Message
    Args: A ros message, if your subscriber is configured properly it should be JointState
    Returns: Nothing
    '''
    # TODO: print the message header. 
    # TODO: convert the joint positions to a numpy array. 
    # TODO: print the joint positions. 
    return 

if __name__ == '__main__':

    # TODO: initialize the node, registering it with the ROS master. 
    # TODO: create a Subscriber to "/robot/joint_states" that calls the callback function above. 
    rospy.spin()