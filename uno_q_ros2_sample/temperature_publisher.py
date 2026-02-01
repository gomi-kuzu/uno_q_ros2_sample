#!/usr/bin/env python3
"""
Temperature Publisher Node for Arduino UNO Q

This node reads temperature data from Arduino UNO Q MCU
and publishes it every 1 second.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

from arduino.app_utils.bridge import call
from arduino.app_utils import App


# Define the bridge function to get temperature from MCU
@call("get_temperature")
def get_sensor_value() -> float: ...


class TemperaturePublisher(Node):
    """ROS2 Node that publishes temperature from Arduino UNO Q MCU."""

    def __init__(self):
        super().__init__('temperature_publisher')
        
        # Create publisher for temperature data
        self.publisher_ = self.create_publisher(
            Float32,
            'uno_q/temperature',
            10
        )
        
        # Create timer for 1 second interval
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.get_logger().info('Temperature Publisher Node has been started')
        self.get_logger().info('Publishing temperature to topic: uno_q/temperature')

    def timer_callback(self):
        """Timer callback that reads and publishes temperature."""
        try:
            # Get temperature from MCU
            temperature = get_sensor_value()
            
            # Create and publish message
            msg = Float32()
            msg.data = float(temperature)
            self.publisher_.publish(msg)
            
            self.get_logger().info(f'Published temperature: {temperature:.2f}')
            
        except Exception as e:
            self.get_logger().error(f'Failed to read temperature: {str(e)}')


def main(args=None):
    """Main function to run the temperature publisher node."""
    # Initialize the Arduino App bridge
    # Note: App.run() is typically blocking, so we need to handle this differently
    # The bridge should be initialized before ROS2 starts
    
    rclpy.init(args=args)
    
    node = TemperaturePublisher()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down temperature publisher node...')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
