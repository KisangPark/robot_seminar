"""
basic example launch file

"""

# 1. import required packages
import os

# necessary tools
from launch_ros.actions import Node
from launch import LaunchDescription


# get other launch files, execute other processes
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.actions import SetLaunchConfiguration, DeclareLaunchArgument, SetEnvironmentVariable
# other launch file sources
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration # can be replaced by declarelaunchargument

# file path searches
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch_ros.substitutions import FindPackageShare


# 2. generate launch description
def generate_launch_description():
    package_name = "basic_example"

    # workspace package path (shared directory)
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