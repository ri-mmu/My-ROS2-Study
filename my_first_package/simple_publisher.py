import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        # 노드 이름을 'simple_publisher'로 초기화
        super().__init__('simple_publisher')
        # 'topic_name'이라는 토픽으로 String 메시지를 보내는 퍼블리셔 생성 (큐 사이즈 10)
        self.publisher_ = self.create_publisher(String, 'topic_name', 10)
        # 1초마다 timer_callback 함수를 실행
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello ROS2! CS231n fighting!'
        self.publisher_.publish(msg)
        # 터미널에 로그 출력 (딥러닝의 print(loss) 같은 역할)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)      # ROS2 통신 초기화
    node = SimplePublisher()   # 노드 생성
    try:
        rclpy.spin(node)       # 노드를 실행 상태로 유지
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()    # 노드 종료
        rclpy.shutdown()       # 통신 종료
