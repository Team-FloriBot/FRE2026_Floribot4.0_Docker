FROM ros:jazzy

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    ros-jazzy-rclpy \
    ros-jazzy-geometry-msgs \
    ros-jazzy-sensor-msgs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /ros2_ws

COPY . /ros2_ws/src/FRE2026_Tasks

RUN pip3 install --no-cache-dir numpy

RUN . /opt/ros/jazzy/setup.sh && \
    colcon build

COPY tasks/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["ros2", "launch", "maize_navigation", "maize_navigation.launch.py"]
