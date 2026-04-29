define flori_lidar ranger
(
  sensor
  (
    range [ 0.10 30.0 ]
    fov 180.0
    samples 720
  )

  size [ 0.07 0.07 0.05 ]
  color "black"
)

define flori_lidar_body flori_lidar
(
  block
  (
    points 8
    point[0] [ 0.035 0.000 ]
    point[1] [ 0.025 0.025 ]
    point[2] [ 0.000 0.035 ]
    point[3] [ -0.025 0.025 ]
    point[4] [ -0.035 0.000 ]
    point[5] [ -0.025 -0.025 ]
    point[6] [ 0.000 -0.035 ]
    point[7] [ 0.025 -0.025 ]
    z [ 0.36 0.41 ]
  )
)

define flori_camera_marker model
(
  size [ 0.06 0.035 0.035 ]
  color "black"

  block
  (
    points 4
    point[0] [ -0.03 -0.0175 ]
    point[1] [  0.03 -0.0175 ]
    point[2] [  0.03  0.0175 ]
    point[3] [ -0.03  0.0175 ]
    z [ 0.47 0.505 ]
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

  # Gelenk / Mittelteil
  block
  (
    points 4
    point[0] [ -0.080 -0.030 ]
    point[1] [  0.080 -0.030 ]
    point[2] [  0.080  0.030 ]
    point[3] [ -0.080  0.030 ]
    z [ 0.18 0.28 ]
  )

  # Räder
  block
  (
    points 4
    point[0] [ -0.39  0.122 ]
    point[1] [ -0.13  0.122 ]
    point[2] [ -0.13  0.212 ]
    point[3] [ -0.39  0.212 ]
    z [ 0.00 0.28 ]
  )

  block
  (
    points 4
    point[0] [ -0.39 -0.212 ]
    point[1] [ -0.13 -0.212 ]
    point[2] [ -0.13 -0.122 ]
    point[3] [ -0.39 -0.122 ]
    z [ 0.00 0.28 ]
  )

  block
  (
    points 4
    point[0] [ 0.13  0.122 ]
    point[1] [ 0.39  0.122 ]
    point[2] [ 0.39  0.212 ]
    point[3] [ 0.13  0.212 ]
    z [ 0.00 0.28 ]
  )

  block
  (
    points 4
    point[0] [ 0.13 -0.212 ]
    point[1] [ 0.39 -0.212 ]
    point[2] [ 0.39 -0.122 ]
    point[3] [ 0.13 -0.122 ]
    z [ 0.00 0.28 ]
  )

  mass 62.4

  drive "diff"
  localization "odom"
  odom_error [ 0.03 0.03 0.00 0.05 ]

  # Front-Lidar
  flori_lidar_body
  (
    name "scan_front"
    pose [ -0.34 0 0.36 0 ]
  )

  # Rear-Lidar
  flori_lidar_body
  (
    name "scan_rear"
    pose [ 0.34 0 0.36 180 ]
  )

  # nur optische Marker, keine echte Kamera in Stage
  flori_camera_marker
  (
    name "camera_front_marker"
    pose [ -0.34 0 0.47 0 ]
  )

  flori_camera_marker
  (
    name "camera_rear_marker"
    pose [ 0.34 0 0.47 180 ]
  )
)
