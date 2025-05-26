"""
Topic converter
    - convert joint state into float
"""

# basic packages
import numpy as np

# rclpy & Node object
import rclpy
from rclpy.node import Node

# standard messages
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from rclpy.qos import QoSProfile

import time

# 1. node object creation: succeeds node object
class TOPIC_CONVERTER(Node):
    def __init__(self):
        super().__init__('topic_converter')
        qos_profile = QoSProfile(depth=10) # history 10 saved, rest default

        # declare subscriber
        self.subscriber = self.create_subscription(JointState, "/joint_states", self.convert, qos_profile)

        # declare publisher, create timer
        self.publisher_1 = self.create_publisher(Float64, "/ign_export/j1_pos", qos_profile)
        self.publisher_2 = self.create_publisher(Float64, "/ign_export/j2_pos", qos_profile)
        self.publisher_3 = self.create_publisher(Float64, "/ign_export/j3_pos", qos_profile)
        self.publisher_4 = self.create_publisher(Float64, "/ign_export/j4_pos", qos_profile)
        self.publisher_5 = self.create_publisher(Float64, "/ign_export/j5_pos", qos_profile)
        self.publisher_6 = self.create_publisher(Float64, "/ign_export/j6_pos", qos_profile)

        self.timer_1 = self.create_timer(0.1, self.publish)


    def convert (self, msg):
        # convert JointState message into float messages
        
        # save joint data
        d

    # timer callback
    def publish(self):

        # generate text
        msg_1 = Float64()

        # flag
        flag = np.random.randint(0, 2)

        # number
        if flag == 1:
            number = 3.1
        else:
            number = 2.5

        msg_1.data = number

        self.publisher_1.publish(msg_1)


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