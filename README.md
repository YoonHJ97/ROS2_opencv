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
## Set parameters
---
size.yaml  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/a5dba682-7afd-4763-b36f-0cef20e3d227)  
fliter.yaml  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/b4ae5d82-7f0e-4603-b33a-ec284dc99dc1)  
server.yaml  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/1e2ded0f-a7d2-4f07-931b-d57aec06a718)  



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

## RQT
---
/camera  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/d0d7d6c9-4813-40c6-8921-633a707f8f4b)  
  
/cannyedge  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/f70cf6ad-529a-4c55-9ef0-a4b29c7e4a81)  
  
/overlay  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/81681f34-6771-4bfe-8fc5-d711f740240a)  



## Capture Image
---
There are three Topics.  
[/camera, /cannyedge, /overlay]


```bash
ros2 service call /capture_image oneday_project_msgs/srv/CaptureImage {"topic: Topic_name"}
```














