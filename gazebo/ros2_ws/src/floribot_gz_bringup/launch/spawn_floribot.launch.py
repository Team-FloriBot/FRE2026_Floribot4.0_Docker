from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch_ros.actions import Node


def generate_launch_description():
    xacro_file = "/ws/src/floribot_gz_description/urdf/Floribot_gz.urdf.xacro"
    rendered_urdf = "/tmp/floribot_gz.urdf"

    robot_description = {
        "robot_description": Command(["xacro ", xacro_file])
    }

    state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[robot_description],
        output="screen",
    )

    render_robot = ExecuteProcess(
        cmd=[
            "bash", "-lc",
            f"source /ws/install/setup.bash && xacro {xacro_file} > {rendered_urdf}"
        ],
        output="screen",
    )

    spawn_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource("/root/.ros/virtual_maize_field/robot_spawner.launch.py"),
        launch_arguments={
            "world": "virtual_maize_field",
            "file": rendered_urdf,
            "entity_name": "floribot4",
        }.items(),
    )

    return LaunchDescription([
        state_publisher,
        render_robot,
        TimerAction(
            period=3.0,
            actions=[spawn_robot],
        ),
    ])
