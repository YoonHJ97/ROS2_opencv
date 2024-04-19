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
## Node Information
---
- ImgPublisher
-- Publishing a Image topic named '/camera'.
  
- cannyedge
-- Subsrcibe '/camera' topic
-- Publishing a topic named '/cannyedge' with canny edge filter applied to the images.
  
- overlay
-- Subsrcibe '/camera', '/cannyedge' topic
-- Publishing images on the topic named '/overlay', with the Canny edge filter applied to the original images.  
  
## Modifying parameters
---
- size.yaml  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/a5dba682-7afd-4763-b36f-0cef20e3d227)  
-- set
  
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
  
  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/1e633c8b-e830-4509-80a3-c8de878e12c8)  
  

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
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/f6ace3b5-0229-4c73-a820-d0c6496f092a)  

![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/0853134b-74ea-459b-ad40-08fc6964352b)  
  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/1476cf6c-84df-4a95-8786-90a40eb7acc4)
