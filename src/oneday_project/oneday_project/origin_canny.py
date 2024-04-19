import cv2
import numpy

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Overlay(Node):
    def __init__(self):
        super().__init__('overlay')

        self.declare_parameter('alpha', 0.7)
        self.alpha = self.get_parameter('alpha').value
        self.declare_parameter('beta', 0.3)
        self.beta = self.get_parameter('beta').value
        self.declare_parameter('gamma', 0)
        self.gamma = self.get_parameter('gamma').value
        
        self.img_subscriber = self.create_subscription(
            Image,
            '/camera', # 이미지 토픽
            self.image_callback,
            10
        )
        self.edge_subscriber = self.create_subscription(
            Image,
            '/cannyedge', # 이미지 토픽
            self.edge_callback,
            10
        )

        self.canny_edge_img = None

        self.cannyedge = self.create_publisher(Image, '/overlay', 10)

        self.cv_bridge = CvBridge()

    def image_callback(self, msg):
        img = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        if self.canny_edge_img is not None :
            edges = self.cv_bridge.imgmsg_to_cv2(self.canny_edge_img, desired_encoding='mono8')
            overlay_img = cv2.addWeighted(img, self.alpha, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR), self.beta, self.gamma)
            overlay_img_msg = self.cv_bridge.cv2_to_imgmsg(overlay_img, encoding='bgr8')
            self.cannyedge.publish(overlay_img_msg)

    def edge_callback(self, msg):
        self.canny_edge_img = msg

def main():
    rclpy.init()

    node = Overlay()

    rclpy.spin(node)

    node.destroy_node()
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()
 

        