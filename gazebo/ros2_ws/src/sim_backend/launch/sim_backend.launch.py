from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    publish_rate_hz_arg = DeclareLaunchArgument(
        "publish_rate_hz",
        default_value="20.0",
    )
    speed_response_alpha_arg = DeclareLaunchArgument(
        "speed_response_alpha",
        default_value="0.25",
    )
    body_angle_gain_arg = DeclareLaunchArgument(
        "body_angle_gain",
        default_value="0.02",
    )
    body_angle_limit_rad_arg = DeclareLaunchArgument(
        "body_angle_limit_rad",
        default_value="0.35",
    )
    publish_body_angle_arg = DeclareLaunchArgument(
        "publish_body_angle",
        default_value="true",
    )
    body_angle_fixed_rad_arg = DeclareLaunchArgument(
        "body_angle_fixed_rad",
        default_value="0.0",
    )

    node = Node(
        package="sim_backend",
        executable="sim_backend_node",
        name="sim_backend",
        output="screen",
        parameters=[
            {
                "publish_rate_hz": LaunchConfiguration("publish_rate_hz"),
                "speed_response_alpha": LaunchConfiguration("speed_response_alpha"),
                "body_angle_gain": LaunchConfiguration("body_angle_gain"),
                "body_angle_limit_rad": LaunchConfiguration("body_angle_limit_rad"),
                "publish_body_angle": LaunchConfiguration("publish_body_angle"),
                "body_angle_fixed_rad": LaunchConfiguration("body_angle_fixed_rad"),
            }
        ],
    )

    return LaunchDescription(
        [
            publish_rate_hz_arg,
            speed_response_alpha_arg,
            body_angle_gain_arg,
            body_angle_limit_rad_arg,
            publish_body_angle_arg,
            body_angle_fixed_rad_arg,
            node,
        ]
    )
