define flori_laser ranger
(
  sensor
  (
    range [ 0.10 30.0 ]
    fov 180.0
    samples 720
  )

  color "blue"
  size [ 0.07 0.07 0.05 ]
)

define flori_laser_body flori_laser
(
  block
  (
    points 8
    point[0] [  0.035  0.000 ]
    point[1] [  0.025  0.025 ]
    point[2] [  0.000  0.035 ]
    point[3] [ -0.025  0.025 ]
    point[4] [ -0.035  0.000 ]
    point[5] [ -0.025 -0.025 ]
    point[6] [  0.000 -0.035 ]
    point[7] [  0.025 -0.025 ]
    z [ 0.335 0.385 ]
  )
)

define floribot position
(
  size [ 1.36 0.43 0.50 ]
  gui_nose 1
  color "gray30"

  # Vorderwagen
  block
  (
    points 4
    point[0] [ -0.675 -0.1065 ]
    point[1] [ -0.040 -0.1065 ]
    point[2] [ -0.040  0.1065 ]
    point[3] [ -0.675  0.1065 ]
    z [ 0.14 0.503 ]
  )

  # Hinterwagen
  block
  (
    points 4
    point[0] [ 0.080 -0.1065 ]
    point[1] [ 0.685 -0.1065 ]
    point[2] [ 0.685  0.1065 ]
    point[3] [ 0.080  0.1065 ]
    z [ 0.14 0.503 ]
  )

  # Gelenk
  block
  (
    points 4
    point[0] [ -0.080 -0.030 ]
    point[1] [  0.080 -0.030 ]
    point[2] [  0.080  0.030 ]
    point[3] [ -0.080  0.030 ]
    z [ 0.18 0.28 ]
  )

  mass 62.4
  drive "diff"
  localization "odom"
  odom_error [ 0.03 0.03 0.00 0.05 ]

  # Gazebo:
  # front_sensor_x = -0.34
  # rear_sensor_x  =  0.34
  # sensor_z       =  0.36

  flori_laser_body
  (
    name "scan_front"
    pose [ -0.34 0 0.36 0 ]
  )

  flori_laser_body
  (
    name "scan_rear"
    pose [ 0.34 0 0.36 180 ]
  )
)
