"""template for launch file"""

# 1. import required packages
import os
from ament_index_python.packages import get_package_share_directory
# from launch
from launch.actions import (DeclareLaunchArgument, SetEnvironmentVariable, 
                            IncludeLaunchDescription, SetLaunchConfiguration)
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, TextSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
#from launch_ros
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


# 2. generate launch description
def generate_launch_description():
    package_name = "package_name"

    # workspace package path
    pkg_path = os.path.join(get_package_share_directory(package_name))

    # include nodes we want to execute
    node_1 = Node(
    package=package_name,
    executable='executable_name_1',
    name='same with executable_name_1',
    )

    node_2 = Node(
    package=package_name,
    executable='executable_name_2',
    name='same with executable_name_2',
    )


    return LaunchDescription(
        [
            node_1,
            node_2,
        ]
    )