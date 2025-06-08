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
        
        # save joint position according to name
        self.joint_position_list = np.zeros(len(msg.name))
        # self.get_logger().info(f"message length: {len(msg.position)}")

        """
        header 
        string list name
        float list position
        float list velocity
        float 64 effort
        """
        for i, joint_name in enumerate(msg.name):

            # replace string to index
            index = int(joint_name.replace("joint", ""))
            # self.get_logger().info(f"index number: {i}, {index-1}")
            self.joint_position_list[index - 1] = msg.position[i-1]

        # joint position saved in order


    # timer callback
    def publish(self):

        # generate list of message
        publisher_list = [self.publisher_1, self.publisher_2, self.publisher_3,
        self.publisher_4, self.publisher_5, self.publisher_6]

        for i, publisher in enumerate(publisher_list):

            # generate Float message, publish

            msg = Float64()

            try:
                msg.data = self.joint_position_list[i]
            except:
                msg.data = 0.0
            
            publisher.publish(msg)

        


# main code -> spin
def main():
    rclpy.init(args=None)
    node = TOPIC_CONVERTER()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    """main function"""
    main()