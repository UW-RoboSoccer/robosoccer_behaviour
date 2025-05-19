from setuptools import setup

package_name = 'behavior'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools', 'rclpy', 'std_msgs'],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    zip_safe=True,
    maintainer='UWRS',
    maintainer_email='uwrobosoccer@gmail.com',
    description='Behavior tree node for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'behavior_tree_node = behavior.behavior_tree_node:main',
        ],
    },
)