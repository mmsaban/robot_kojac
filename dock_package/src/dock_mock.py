import subprocess

def send_dock_goal():
    action_command = "ros2 action send_goal /dock irobot_create_msgs/action/Dock '{}'"
    subprocess.run(action_command, shell=True)

if __name__ == "__main__":
    send_dock_goal()
