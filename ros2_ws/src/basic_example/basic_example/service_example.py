"""example code for service server node"""

# 1. import rclpy, node and messages
import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
from rclpy.qos import QoSProfile

# 2. define service node
class SERVICE_NODE(Node):

    def __init__(self):

        # inherit "Node" object, set node name
        super().__init__("service_node")

        # set qos profile (communication settings)
        qos_profile = QoSProfile(depth=10)

        # create server
        self.server = self.create_service(Trigger, 'trigger', self.callback)

    # server got request, callback
    def callback(self, request, response):

        # make response
        response.success = True
        response.message = "Service call success"

        # send response
        self.get_logger().info("Service call success")

        return response


# 3. main function to execute
def main():

    # rclpy initialization at very first
    rclpy.init(args=None)

    # declare node
    my_node = SERVICE_NODE()

    # spin node
    rclpy.spin(my_node)

    # when end, destroy node and shutdown
    my_node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()