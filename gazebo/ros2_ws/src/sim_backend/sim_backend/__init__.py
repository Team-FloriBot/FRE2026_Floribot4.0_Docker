        self.front_left_cmd_pub = self.create_publisher(
            Float64, "/sim/joint_frontLeft/cmd_vel", 10
        )
        self.front_right_cmd_pub = self.create_publisher(
            Float64, "/sim/joint_frontRight/cmd_vel", 10
        )
        self.rear_left_cmd_pub = self.create_publisher(
            Float64, "/sim/joint_rearLeft/cmd_vel", 10
        )
        self.rear_right_cmd_pub = self.create_publisher(
            Float64, "/sim/joint_rearRight/cmd_vel", 10
        )
