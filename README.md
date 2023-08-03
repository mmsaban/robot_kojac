# dock_package

## Overview

This ROS 2 package implements a simple Battery Monitor Node that subscribes to the `/battery_state` topic and triggers an action to dock the robot when the battery percentage falls below a certain threshold. The action is sent using the `ros2 action send_goal` command.

## Prerequisites

- ROS 2 Galactic Geochelone or later
- Python 3.x
- `irobot_create_msgs` package
- Action server for the `/dock` action

## Installation

1. Clone this package into your ROS 2 workspace (e.g., `create3_ws/src`):

   ```bash
   git clone <url-to-dock_package.git> create3_ws/src/dock_package
