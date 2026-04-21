from setuptools import find_packages, setup

package_name = "sim_backend"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml"]),
        (f"share/{package_name}/launch", ["launch/sim_backend.launch.py"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="FloriBot Team",
    maintainer_email="team@floribot.local",
    description="Simulation backend for FloriBot base topics.",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "sim_backend_node = sim_backend.sim_backend_node:main",
        ],
    },
)
