"""template for node file"""


# 1. import rclpy, node and messages
import rclpy
from rclpy.node import node
from std_msgs.msg import Int32
from rclpy.qos import QoSProfile

# additional python imports


# 2. define user node
class USER_NODE(Node):

    def __init__(self):

        # inherit "Node" object, set node name
        super().__init__("node_name")

        # set qos profile (communication settings)
        qos_profile = QoSProfile(depth=10)

        # create subscriber
        self.subscriber = self.create_subscription(ros2_format, "/topic_name", self.sub_callback, qos_profile)
        self.subscriber # error avoidance

        # create publisher
        self.publisher = self.create_publisher(ros2_format, "/topic_name", qos_profile)

        # create timer, to execute callback repeatedly
        self.timer = self.create_timer(frequency, self.pub_callback)


    # subscription callback
    def sub_callback(self, msg):
        # your code here

    
    # publisher callback
    def pub_callback(self):
        # your code here
        self.publisher.publish()




# 3. main function to execute
def main():

    # rclpy initialization at very first
    rclpy.init(args=None)

    # declare node
    my_node = USER_NODE()

    # spin node
    rclpy.spin(my_node)

    # when end, destroy node and shutdown
    my_node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()