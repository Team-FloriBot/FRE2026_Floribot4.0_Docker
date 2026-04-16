from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    spawn_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource("/root/.ros/virtual_maize_field/robot_spawner.launch.py"),
        launch_arguments={
            "world": "virtual_maize_field",
            "file": "/ws/src/floribot_gz_description/models/floribot_test.sdf",
            "entity_name": "floribot4",
        }.items(),
    )

    return LaunchDescription([
        spawn_robot,
    ])
