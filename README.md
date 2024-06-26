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
  - Publishing a Image topic named '/camera'.
  
- cannyedge
  - Subsrcibe '/camera' topic
  - Publishing a topic named '/cannyedge' with canny edge filter applied to the images.
  
- overlay
  - Subsrcibe '/camera', '/cannyedge' topic
  - Publishing images on the topic named '/overlay', with the Canny edge filter applied to the original images.  
  
## Modifying parameters
---
- size.yaml  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/a5dba682-7afd-4763-b36f-0cef20e3d227)  
  - Set Image topic size
  
- fliter.yaml  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/b4ae5d82-7f0e-4603-b33a-ec284dc99dc1)  
threshold_1 and threshold_2 are the threshold values used in the Canny edge detector.  
  - threshold_1: If the gradient intensity is higher than the threshold, it is considered as an edge. Lower values detect more edges but also generate more noise.
  - threshold_2: If the gradient intensity is lower than the threshold, it is not considered as an edge. Higher values generate fewer but stronger edges.
  
  Alpha, Beta, and Gamma play the following roles:  
    - Alpha: It's the weight applied to the original image. A higher value makes the original image more dominant.
    - Beta: It's the weight applied to the edges detected. A higher value emphasizes the edges more.
    - Gamma: An additional value added to the computed weighted sum. Typically, it's 0.

- server.yaml  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/1e2ded0f-a7d2-4f07-931b-d57aec06a718)  
  - The path to save the image


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
  
![image](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/d438a933-f7e5-436a-9d3a-f4b73c3c0503)




![GIFMaker_me (1)](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/be2690f6-973f-4a25-9821-bb1c444d388d)  
![GIFMaker_me](https://github.com/YoonHJ97/ROS2_opencv/assets/162243554/edbb8878-47be-4f65-bffe-9a0dbd8fbd34)  






