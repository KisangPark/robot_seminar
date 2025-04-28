"""template for launch file"""

# 1. import required packages
import os
from ament_index_python.packages import get_package_share_directory
# from launch
from launch import LaunchDescription
from launch.actions import (DeclareLaunchArgument, SetEnvironmentVariable, 
                            IncludeLaunchDescription, SetLaunchConfiguration)
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, TextSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
#from launch_ros
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


# 2. generate launch description
def generate_launch_description():
    package_name = "tutorial"

    # workspace package path
    pkg_path = os.path.join(get_package_share_directory(package_name))

    # include nodes we want to execute
    sub = Node(
    package=package_name,
    executable='subscriber_example',
    name='subscriber_example',
    )

    pub = Node(
    package=package_name,
    executable='publisher_example',
    name='publisher_example',
    )


    return LaunchDescription(
        [
            sub,
            pub,
        ]
    )