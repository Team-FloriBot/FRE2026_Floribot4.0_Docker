from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler, TimerAction
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    xacro_file = "/ws/src/floribot_gz_description/urdf/Floribot_gz.urdf.xacro"
    rendered_urdf = "/tmp/floribot_gz.urdf"

    world_launch = PathJoinSubstitution([
        FindPackageShare("virtual_maize_field"),
        "launch",
        "simulation.launch.py",
    ])

    robot_description = {
        "robot_description": Command(["xacro ", xacro_file])
    }

    generate_world = ExecuteProcess(
        cmd=[
            "bash", "-lc",
            "source /ws/install/setup.bash && "
            "ros2 run virtual_maize_field generate_world fre22_task_navigation_mini"
        ],
        output="screen",
    )

    state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[robot_description],
        output="screen",
    )

    start_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(world_launch)
    )

    render_robot_file = ExecuteProcess(
        cmd=[
            "bash", "-lc",
            f"source /ws/install/setup.bash && xacro {xacro_file} > {rendered_urdf}"
        ],
        output="screen",
    )

    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-world", "virtual_maize_field",
            "-name", "floribot4",
            "-file", rendered_urdf,
            "-x", "-1.3631752758808973",
            "-y", "-3.460156696047507",
            "-z", "0.6499999999999999",
            "-R", "0.0",
            "-P", "0.0",
            "-Y", "1.5980816365126524",
        ],
        output="screen",
    )

    return LaunchDescription([
        generate_world,

        RegisterEventHandler(
            OnProcessExit(
                target_action=generate_world,
                on_exit=[
                    start_world,
                    state_publisher,
                    render_robot_file,
                    TimerAction(
                        period=8.0,
                        actions=[spawn_robot],
                    ),
                ],
            )
        ),
    ])
