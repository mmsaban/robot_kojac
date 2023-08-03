import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState  # Import the BatteryState message type
from std_msgs.msg import String
from irobot_create_msgs.action import Dock
import subprocess 


class BatteryMonitorNode(Node):
    def __init__(self):
        super().__init__('battery_monitor')
        self.subscription = self.create_subscription(
            BatteryState,
            '/battery_state',
            self.battery_callback,
            10
        )
        self.publisher_ = self.create_publisher(String, '/battery_status', 10)

    def battery_callback(self, msg):
        # Check the battery percentage and trigger action if too low
        self.publish_status(msg.percentage, '  ')
        if msg.percentage < 0.9991:
#            Dock()
            self.publish_status(msg.percentage, '  is lower and needs to dock')
            self.send_dock_goal()

    def publish_status(self, percentage, text):
        # Publish a message with the battery status
        msg = String()
        msg.data = f'Test Battery Percentage: {percentage}%' + text
        self.publisher_.publish(msg)

    def send_dock_goal(self):
        action_command = "ros2 action send_goal /dock irobot_create_msgs/action/Dock '{}'"
        subprocess.run(action_command, shell=True)


def main(args=None):
    rclpy.init(args=args)
    node = BatteryMonitorNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()    
