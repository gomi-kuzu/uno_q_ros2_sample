# uno_q_ros2_sample

Arduino UNO QでROS2使用を試してみる

## 検証環境
- Debian GNU/Linux 13
- ROS2 Humble(RoboStack)

## ビルド

```bash
cd ~/ros2_ws
colcon build --packages-select uno_q_ros2_sample
source install/setup.bash
```