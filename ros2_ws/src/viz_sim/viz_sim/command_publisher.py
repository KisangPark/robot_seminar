"""
gazebo joint command publisher
use sim time setting check
"""

# basic packages
import numpy as np


# rclpy & Node object
import rclpy
from rclpy.node import Node

# standard messages
from std_msgs.msg import Float64 # ord & chr function
from rclpy.qos import QoSProfile

import time

# 1. node object creation: succeeds node object
class COMMAND_PUBLISHER(Node):
    def __init__(self):
        super().__init__('command_publisher')
        qos_profile = QoSProfile(depth=10) # history 10 saved, rest default

        # declare publisher, create timer
        self.publisher_1 = self.create_publisher(Float64, "/j1_pos", qos_profile)
        self.timer_1 = self.create_timer(2, self.callback)

    # timer callback
    def callback(self):

        # generate text
        msg = Float64()

        # flag
        flag = np.random.randint(0, 2)

        # number
        if flag == 1:
            number = 3.1
        else:
            number = 2.5

        msg.data = number

        self.publisher_1.publish(msg)


# main code -> spin
def main():
    rclpy.init(args=None)
    node = COMMAND_PUBLISHER()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    """main function"""
    main()