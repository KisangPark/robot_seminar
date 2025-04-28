"""example code for subscriber node"""

# 1. import rclpy, node and messages
import rclpy
from rclpy.node import node
from std_msgs.msg import Int32
from rclpy.qos import QoSProfile

# 2. define user node
class SUBSCRIBER_NODE(Node):

    def __init__(self):

        # inherit "Node" object, set node name
        super().__init__("subscriber_node")

        # set qos profile (communication settings)
        qos_profile = QoSProfile(depth=10)

        # create subscriber
        self.subscriber_1 = self.create_subscription(Int32, "/int_topic", self.callback, qos_profile)
        self.subscriber_1 # error avoidance

    # subscriber callback
    def callback(self, msg):

        # get message, extract data
        number = msg.data

        # print logger
        self.get_logger().info(f"received data is {number}")


# 3. main function to execute
def main():

    # rclpy initialization at very first
    rclpy.init(args=None)

    # declare node
    my_node = SUBSCRIBER_NODE()

    # spin node
    rclpy.spin(my_node)

    # when end, destroy node and shutdown
    my_node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()