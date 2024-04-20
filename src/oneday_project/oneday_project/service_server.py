import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from oneday_project_msgs.srv import CaptureImage, RecordVideo
from cv_bridge import CvBridge
import cv2
import time

class CaptureImageServer(Node):
    def __init__(self):
        super().__init__('capture_image_server')
        self.srv_capture_image = self.create_service(CaptureImage, 'capture_image', self.capture_image_callback) #client 확인, init에 sub 3개 생성
        self.srv_record_video = self.create_service(RecordVideo, 'record_video', self.record_video_callback) #client 확인, init에 sub 3개 생성

        self.cv_bridge = CvBridge()

        
        self.declare_parameter('path', '/home/hj/amr_ws/ROS/data/')
        self.file_path = self.get_parameter('path').value

        self.sub_camera = self.create_subscription(
            Image,
            "/camera",
            self.camera_callback,
            10
        )
        self.sub_camera = self.create_subscription(
            Image,
            "/cannyedge",
            self.cannyedge_callback,
            10
        )
        self.sub_camera = self.create_subscription(
            Image,
            "/overlay",
            self.overlay_callback,
            10
        )
        self.img_camera = None
        self.img_cannyedge = None
        self.img_overlay = None
        self.camera_record = False
        self.cannyedge_record = False
        self.overlay_record = False
        self.out = None
        self.record_start_time = None
        self.req_time = 0

    def camera_callback(self, msg):
        self.img_camera = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        if self.record_start_time is not None and self.camera_record:
            elapsed_time = time.time() - self.record_start_time
            if elapsed_time <= self.req_time:
                self.out.write(self.img_camera)
            else:
                self.stop_recording()

    def cannyedge_callback(self, msg):
        self.img_cannyedge = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        if self.record_start_time is not None and self.cannyedge_record:
            elapsed_time = time.time() - self.record_start_time
            if elapsed_time <= self.req_time:
                self.out.write(self.img_cannyedge)
            else:
                self.stop_recording()

    def overlay_callback(self, msg):
        self.img_overlay = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        if self.record_start_time is not None and self.overlay_record:
            elapsed_time = time.time() - self.record_start_time
            if elapsed_time <= self.req_time:
                self.out.write(self.img_overlay)
            else:
                self.stop_recording()
                
    def capture_image_callback(self, request, response):
        topic = request.topic
        file_name = 'captured_image.jpg'  # 예시 파일 이름
        file_path_with_name = self.file_path + file_name
        self.get_logger().info(f'! file_path: {self.file_path}')
        self.get_logger().info(f'! file_path_with_name: {file_path_with_name}')
        if topic == "/camera":
            cv2.imwrite(file_path_with_name, self.img_camera)
        elif topic == "/cannyedge":
            cv2.imwrite(file_path_with_name, self.img_cannyedge)
        elif topic == "/overlay":
            cv2.imwrite(file_path_with_name, self.img_overlay)
        else:
            # 다른 토픽에 대한 처리
            pass      
        # 이미지 저장 경로를 응답에 설정합니다.
        response.saved_image_path = file_path_with_name

        return response        
    
    def record_video_callback(self, request, response):
        topic = request.topic
        self.req_time = request.time
        file_name = 'recorded_video.avi'
        file_path_with_name = self.file_path + file_name
        
        self.get_logger().info(f'! req_time: {self.req_time}')
        self.get_logger().info(f'! file_path: {self.file_path}')
        self.get_logger().info(f'! file_path_with_name: {file_path_with_name}')

        if topic in ["/camera", "/cannyedge", "/overlay"]:
            frame_width = self.img_camera.shape[1]
            frame_height = self.img_camera.shape[0]

            self.out = cv2.VideoWriter(file_path_with_name, cv2.VideoWriter_fourcc(*'XVID'), 20, (frame_width, frame_height))
            self.record_start_time = time.time()

            # 녹화 상태를 저장합니다.
            if topic == "/camera":
                self.camera_record = True
                self.cannyedge_record = False
                self.overlay_record = False
            elif topic == "/cannyedge":
                self.camera_record = False
                self.cannyedge_record = True
                self.overlay_record = False
            elif topic == "/overlay":
                self.camera_record = False
                self.cannyedge_record = False
                self.overlay_record = True

            response.saved_video_path = file_path_with_name
        else:
            self.get_logger().info("Invalid topic.")

        return response
         
    def stop_recording(self):
        self.out.release()
        self.record_start_time = None
        self.camera_record = False
        self.cannyedge_record = False
        self.overlay_record = False
        self.get_logger().info("End Recording.")
         
         
def main(args=None):
    rclpy.init(args=args)
    capture_node = CaptureImageServer()
    rclpy.spin(capture_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
