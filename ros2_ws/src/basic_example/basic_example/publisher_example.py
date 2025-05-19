"""example code for publisher node"""

# 1. import rclpy, node and messages
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Float32, String
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

        """ multiple topics example: 3 topics """
        # self.publisher_2 = self.create_publisher(Float32, "/ex2/float", qos_profile)
        # self.publisher_3 = self.create_publisher(String, "/ex2/string", qos_profile)

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


        """ multiple topics example: 3 topics """

        # msg2 = Float32()
        # msg2.data = 0.1
        # self.publisher_2.publish(msg2)

        # msg3 = String()
        # msg3.data = "example"
        # self.publisher_3.publish(msg3)



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