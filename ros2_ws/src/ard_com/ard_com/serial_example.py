"""
Arduino Serial communication example

write string to serial, with the frequency of 10Hz
Simultaneously publish ROS2 topic
"""

# basic packages
import numpy as np

# import serial
import serial
serial_out = serial.Serial(port='/dev/ttyACM0', baudrate=9600,)

# rclpy & Node object
import rclpy
from rclpy.node import Node

# standard messages
from std_msgs.msg import Int32 # ord & chr function
from rclpy.qos import QoSProfile

import time

# 1. node object creation: succeeds node object
class SERIAL_WRITER(Node):
    def __init__(self):
        super().__init__('serial_writer_node')
        qos_profile = QoSProfile(depth=10) # history 10 saved, rest default

        # declare publisher, create timer
        self.publisher_1 = self.create_publisher(Int32, "serial_write", qos_profile)
        self.timer_1 = self.create_timer(5, self.write_serial)

    # timer callback
    def write_serial(self):

        # generate text
        msg = Int32()
        number = np.random.randint(70,110)
        msg.data = number
        print(f"random number: {number}")
        text= f"{number}"

        # publish ROS2 topic, get logger
        # self.get_logger().info("random number is %d" %number)
        self.publisher_1.publish(msg)

        # arduino serial write (encoding with ASCII)
        # serial_out.write(number.to_bytes(8, 'big')) # ord function & chr function
        serial_out.write(text.encode())
        time.sleep(1.01)

        # get serial return & visualize (print)
        if serial_out.readable():
            response = serial_out.readline()
            print(response[:len(response)-1].decode())

# main code -> spin
def main():
    rclpy.init(args=None)
    node = SERIAL_WRITER()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    """main function"""
    main()