"""example code for publisher node"""

# 1. import rclpy, node and messages
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from rclpy.qos import QoSProfile

# additional python imports
import numpy as np

# 2. define user node
class PUBLISHER_NODE(Node):

    def __init__(self):

        # inherit "Node" object, set node name
        super().__init__("publisher_node")

        # set qos profile (communication settings)
        qos_profile = QoSProfile(depth=10)

        # create publisher
        self.publisher_1 = self.create_publisher(Int32, "/int_topic", qos_profile)

        # create timer, to execute callback repeatedly
        self.timer = self.create_timer(0.1, self.callback)

    #  timer callback
    def callback(self):

        # make random integer message
        number = np.random.randint(1, 5)

        # make ROS2 format message (refer to ros2 std_msgs documentation)
        msg = Int32()
        msg.data = number

        # **publish message**
        self.publisher_1.publish(msg)



# 3. main function to execute
def main():

    # rclpy initialization at very first
    rclpy.init(args=None)

    # declare node
    my_node = PUBLISHER_NODE()

    # spin node
    rclpy.spin(my_node)

    # when end, destroy node and shutdown
    my_node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()