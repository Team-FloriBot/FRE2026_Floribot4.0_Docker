from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessStart
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
        RegisterEventHandler(
            OnProcessStart(
                target_action=world_launch,
                on_start=[robot_launch],
            )
        ),
    ])
