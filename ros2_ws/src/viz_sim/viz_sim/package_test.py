from ament_index_python.packages import get_package_share_directory


def asdf():
    path = get_package_share_directory('viz_sim')
    print(path)

def main():
    asdf()

if __name__ == '__main__':
    main()



"""
OUTPUT
/home/kisangpark/workspace/robot_seminar/ros2_ws/install/viz_sim/share/viz_sim
"""