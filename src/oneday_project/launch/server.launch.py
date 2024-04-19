import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description(): 
    param_dir = LaunchConfiguration(
        'param_dir',
        default=os.path.join(
        get_package_share_directory('oneday_project'),
        'param',
        'server.yaml')
        )
    
    return LaunchDescription(
        [
            DeclareLaunchArgument( 
                'param_dir',
                default_value=param_dir
            ),

            Node(
                package='oneday_project',
                executable='service_server',
                name='service_server',
                parameters=[param_dir],
                output='screen'),
        ]
    )