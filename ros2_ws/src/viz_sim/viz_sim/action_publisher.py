"""
action publisher
    - random joint state publisher to /joint_command
"""

# basic packages
import numpy as np

# rclpy & Node object
import rclpy
from rclpy.node import Node

# standard messages
from sensor_msgs.msg import JointState
from rclpy.qos import QoSProfile

import time


# 1. node object creation: succeeds node object
class ACTION_PUBLISHER(Node):
    def __init__(self):
        super().__init__('action_publisher')
        qos_profile = QoSProfile(depth=10) # history 10 saved, rest default

        # publisher declaration
        self.publisher = self.create_publisher(JointState, "/joint_command", qos_profile)
        self.timer_1 = self.create_timer(0.1, self.publish)

        self.flag = True
        self.value = 0.0


    def publish (self):

        # generate angle position value
        if self.flag == True:
            self.value += 0.02
            if self.value > 1.0:
                self.flag = False
        else:
            self.value -= 0.02
            if self.value < -1.0:
                self.flag=True


        # make lists -> name, position, velocity, effort

        name, position = [], []

        for i in range(6):
            temp_name = f"joint{i}"
            name.append(temp_name)
            position.append(self.value)

        # publish joint command
        msg = JointState()

        # data
        self.get_logger().info(f"position string: {position}")

        msg.name = name
        msg.position = position
        # msg.velocity = np.zeros(6)
        # msg.effort = np.zeros(6)

        self.publisher.publish(msg)



# main code -> spin
def main():
    rclpy.init(args=None)
    node = ACTION_PUBLISHER()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    """main function"""
    main()