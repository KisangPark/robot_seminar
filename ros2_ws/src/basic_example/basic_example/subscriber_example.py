"""example code for subscriber node"""

# 1. import rclpy, node and messages
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Float32, String
from rclpy.qos import QoSProfile

# 2. define user node
class SUBSCRIBER_NODE(Node):

    def __init__(self):

        # inherit "Node" object, set node name
        super().__init__("subscriber_node")

        # set qos profile (communication settings)
        qos_profile = QoSProfile(depth=10)

        # create subscriber
        self.subscriber_1 = self.create_subscription(Int32, "/int_topic", self.int_callback, qos_profile)
        self.subscriber_1 # error avoidance

        """ multiple topics example: 3 topics """
        # self.subscriber_2 = self.create_subscription(Float32, "/ex2/float", self.float_callback, qos_profile)
        # self.subscriber_3 = self.create_subscription(String, "/ex2/string", self.string_callback, qos_profile)

    # subscriber callback
    def int_callback(self, msg):

        # get message, extract data
        number = msg.data

        # print logger
        self.get_logger().info(f"received data is {number}")


    """ multiple topics example: 3 topics """

    # def float_callback(self, msg):
    #     float_num = msg.data
    #     self.get_logger().info(f"received data is {float_num}")

    # def string_callback(self, msg):
    #     string = msg.data
    #     self.get_logger().info(f"received data is {string}")


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