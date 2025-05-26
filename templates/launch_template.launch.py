"""template for launch file"""

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
    package_name = "package_name"

    # workspace package path
    # share directory path: ros2_ws/install/<package_name>/share/<package_name>
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

    # include launch file to execute
    launch_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory(package_name), "launch", "launch_file_name.launch.py")]),
            launch_arguments = {"arguments_1":"value_1", "arguments_1":"value_2"}.items(),
        )


    # return launch descriptions
    return LaunchDescription(
        [
            node_1,
            node_2,
            launch_1,
        ]
    )