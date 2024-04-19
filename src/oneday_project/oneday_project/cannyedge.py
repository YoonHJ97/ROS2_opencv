import cv2
import numpy

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class CannyEdge(Node):
    def __init__(self):
        super().__init__('cannyedge')

        self.declare_parameter('camera_topic', '/camera')
        
        self.declare_parameter('threshold_1', 100)
        self.threshold_1 = self.get_parameter('threshold_1').value
        self.declare_parameter('threshold_2', 200)
        self.threshold_2 = self.get_parameter('threshold_2').value
        
        self.img_subscriber = self.create_subscription(
            Image,
            '/camera', # 이미지 토픽
            self.image_callback,
            10
        )

        self.cannyedge = self.create_publisher(Image, '/cannyedge', 10)

        self.cv_bridge = CvBridge()

    def image_callback(self, msg):
        img = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        edges = cv2.Canny(img, self.threshold_1, self.threshold_2)
        pub_img = self.cv_bridge.cv2_to_imgmsg(edges, "mono8")
        self.cannyedge.publish(pub_img)


def main():
    rclpy.init()

    node = CannyEdge()

    rclpy.spin(node)

    node.destroy_node()
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()
 

        