# ROS2_opencv
---
## Directory Tree
---
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/f7c9682e-fcb6-468e-af6b-3b1598f4c5da)


# Set Up
---
## To get started


```bash
git clone --recurse-submodules https://github.com/adrian-soch/ros_vision_track.git
```

## Install Python requirements

```bash
pip3 install opencv-python
sudo apt install ros-humble-cv-bridge
```


# Running the Code
---
## Build Workspace
---


```bash
colcon build
```


## Sourcing


```bash
source /opt/ros/humble/setup.bash
source source install/setup.bash
```


## Launch Total Python File
---


```bash
ros2 launch oneday_project total.launch.py 
```

## Capture Image
---
There are three Topics.
[/camera, /cannyedge, /overlay]


```bash
ros2 service call /capture_image oneday_project_msgs/srv/CaptureImage {"topic: Topic_name"}
```














