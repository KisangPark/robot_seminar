"""
loading sdf files & launch gazebo
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
    #use sim time
    # use_sim_time = LaunchConfiguration("use_sim_time")

    # package path
    pkg_path = os.path.join('/home/kisangpark/workspace/robot_seminar/ros2_ws/src/viz_sim')
    share_pkg_path = os.path.join(get_package_share_directory('viz_sim'))

    # sdf path
    world_path = os.path.join(pkg_path, 'xacro', 'empty.world')
    robot_path = os.path.join(pkg_path, 'xacro', 'arm.sdf')

    # launch gazebo with ros_gz_sim
    sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('ros_gz_sim'), "launch", "gz_sim.launch.py")]),
            launch_arguments = {"use_sim_time":"true", "gz_args":world_path}.items(),
        )

    # node for robot sdf
    create_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments = [
            '-world', 'my_world',
            '-name','arm',
            '-file', robot_path,
            '-x', '0', '-y', '0', '-z', '0.5'
        ],
        output='screen'
    )


# launch description return
    return LaunchDescription([
        # 1-1. empty gazebo world
        # sim,
        ExecuteProcess(
            cmd=['ign', 'gazebo', world_path], # , '--verbose'
            output='screen'
        ),

        # # 1-2. delay, waiting gazebo to be ready
        # ExecuteProcess(
        #     cmd=['sleep', '3'],
        #     shell=True
        # ),


        # 2. robot sdf file spawn
        # create_robot,
    ])
