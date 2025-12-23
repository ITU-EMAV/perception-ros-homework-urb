from setuptools import find_packages, setup
from glob       import glob
import os

package_name = 'perception_ros'
csv_file = 'placeholder.csv'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name,'Perception','Perception.model','Perception.utils'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['share/' + package_name + '/' + csv_file]),
        ('share/' + package_name + '/launch', ['launch/perception_ros_launch.py']),
        ('share/' + package_name + '/Perception', glob('Perception/*.pt'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='emav',
    maintainer_email='emav@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'perception = perception_ros.perception:main',
        'controller = perception_ros.controller:main',
        'position = perception_ros.position:main',
        'track = perception_ros.track:main',
        'error_recorder = perception_ros.error:main',
        'steering_recorder = perception_ros.steer:main',
        'velocity_recorder = perception_ros.velocity:main'
        # 'live_map = perception_ros.live_map:main' 
        ],
    },
)
