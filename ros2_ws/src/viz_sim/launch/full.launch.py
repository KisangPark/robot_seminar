"""
Launch all!
"""

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



# generate launch description
def generate_launch_description():


    # launch gz_ctrl
    gz_ctrl = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('viz_sim'), "launch", "gz_ctrl.launch.py")]),
        )

    # launch rsp
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('viz_sim'), "launch", "rsp.launch.py")]),
        )


    # topic converter node
    topic_converter = Node(
        package='viz_sim',
        executable='topic_converter',
        output='screen'
    )

    # action publisher node
    action_publisher = Node(
        package='viz_sim',
        executable='action_publisher',
        output='screen'
    )


# launch description return
    return LaunchDescription([

        # launch - gazebo
        gz_ctrl, 

        # launch - rsp
        rsp,

        # node - topic converter
        topic_converter,

        # node - action publisher
        action_publisher,

    ])
