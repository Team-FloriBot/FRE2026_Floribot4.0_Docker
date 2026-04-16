from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    bringup_launch_dir = os.path.join(
        get_package_share_directory("floribot_gz_bringup"),
        "launch",
    )

    world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(bringup_launch_dir, "maize_world.launch.py")
        )
    )

    robot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(bringup_launch_dir, "spawn_floribot.launch.py")
        )
    )

    return LaunchDescription([
        world_launch,
        TimerAction(
            period=8.0,
            actions=[robot_launch],
        ),
    ])
