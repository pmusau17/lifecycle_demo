from launch import LaunchDescription
from launch_ros.actions import LifecycleNode
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        LifecycleNode(package='lifecycle_demo', 
                      executable='lifecycle_dummy_pub',
                      arguments=["carma_dummy_pub"],
                      name='carma_dummy_pub',
                      output='screen'),
        Node(package='lifecycle_demo', 
             executable='lifecycle_dummy_sub', 
             arguments=["carma_dummy_sub","carma_dummy_pub"],
             name='carma_dummy_sub',
             output='screen'),
        Node(package='lifecycle_demo', 
             executable='lifecycle_manager', 
             name='carma_dummy_manager',
             arguments=["carma_dummy_manager","carma_dummy_pub"],
             output='screen')
    ])