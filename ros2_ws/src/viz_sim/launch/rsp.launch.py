"""
Launch file for ROS
    1) Rviz2
    2) Robot State Publisher
    3) Joint State Publisher
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


def generate_launch_description():
    # seminar directory
    seminar_directory = '/home/kisangpark/workspace/robot_seminar'

    # package path
    pkg_path = os.path.join(seminar_directory, 'ros2_ws', 'src', 'viz_sim')
    share_pkg_path = os.path.join(get_package_share_directory('viz_sim'))

    # robot sdf path
    robot_path = os.path.join(share_pkg_path, 'sdf_model', 'robotic_arm.sdf')

    # rviz2 configuration path
    rviz_path = os.path.join(seminar_directory, 'configure', 'arm.rviz')


    # open sdf file -> make robot description
    with open(robot_path, 'r') as rf:
        robot_desc = rf.read()

    # joint state publisher node
    jsp = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        arguments=[robot_path],
        output='screen',
        parameters=[
            {"source_list": ["joint_command"]}
        ]
    )

    # robot state publisher node
    rsp = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    name='robot_state_publisher',
    output='both',
    parameters=[
        {'use_sim_time': True,
        'robot_description': robot_desc},
    ]
    )

    # rviz node
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=["--display-config", rviz_path]
    )


    return LaunchDescription(
        [
            rsp,
            jsp,
            rviz,
        ]
    )

