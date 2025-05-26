"""
Arduino Serial communication example
    - write string to serial & Simultaneously publish ROS2 topic
    - receive string from serial & convert to integer

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
        qos_profile = QoSProfile(depth=10)

        # declare publisher, create timer
        self.publisher_1 = self.create_publisher(Int32, "serial_write", qos_profile) # publish "serial_write" topic
        self.timer_1 = self.create_timer(0.1, self.write_serial)


    # timer callback
    def write_serial(self):

        # declare ROS2 topic
        msg = Int32()

        # generate servo angle
        number = np.random.randint(70,110)
        msg.data = number
        print(f"python-generated random number: {number}")

        # convert integer into text using f string
        text= f"{number}"

        # publish ROS2 topic
        self.publisher_1.publish(msg)

        # get logger
        # self.get_logger().info("random number is %d" %number)
        

        # arduino serial write (encoding with ASCII)
        serial_out.write(text.encode()) # encode string to bytes
        
        # wait during arduino process
        time.sleep(0.21) 

        # get serial return & print
        if serial_out.readable():
            
            # receive bytes (= string)
            response = serial_out.readline() 

            # decode response, convert to integer
            received_data = int(response[:len(response)-1].decode())
            print("python received:", received_data)



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