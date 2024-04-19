import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # 각 노드에 대한 파라미터 파일 경로 설정
    img_publisher_param_dir = LaunchConfiguration(
        'img_publisher_param_dir',
        default=os.path.join(
            get_package_share_directory('oneday_project'),
            'param',
            'size.yaml')
    )
    cannyedge_param_dir = LaunchConfiguration(
        'cannyedge_param_dir',
        default=os.path.join(
            get_package_share_directory('oneday_project'),
            'param',
            'filter.yaml')
    )
    origin_canny_param_dir = LaunchConfiguration(
        'origin_canny_param_dir',
        default=os.path.join(
            get_package_share_directory('oneday_project'),
            'param',
            'filter.yaml')
    )
    service_server_param_dir = LaunchConfiguration(
        'service_server_param_dir',
        default=os.path.join(
            get_package_share_directory('oneday_project'),
            'param',
            'server.yaml')
    )

    return LaunchDescription([
        # img_publisher 노드 실행
        DeclareLaunchArgument(
            'img_publisher_param_dir',
            default_value=img_publisher_param_dir
        ),
        Node(
            package='oneday_project',
            executable='img_publisher',
            name='img_publisher',
            parameters=[img_publisher_param_dir],
            output='screen'
        ),
        # cannyedge 노드 실행
        DeclareLaunchArgument(
            'cannyedge_param_dir',
            default_value=cannyedge_param_dir
        ),
        Node(
            package='oneday_project',
            executable='cannyedge',
            name='cannyedge',
            parameters=[cannyedge_param_dir],
            output='screen'
        ),
        DeclareLaunchArgument(
            'origin_canny_param_dir',
            default_value=origin_canny_param_dir
        ),
        # origin_canny 노드 실행
        Node(
            package='oneday_project',
            executable='origin_canny',
            name='overlay',
            parameters=[origin_canny_param_dir],
            output='screen'
        ),
        # service_server 노드 실행
        DeclareLaunchArgument(
            'service_server_param_dir',
            default_value=service_server_param_dir
        ),
        Node(
            package='oneday_project',
            executable='service_server',
            name='service_server',
            parameters=[service_server_param_dir],
            output='screen'
        )
    ])
