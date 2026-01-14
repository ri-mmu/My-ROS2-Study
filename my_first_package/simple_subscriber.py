import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleSubscriber(Node):
    def __init__(self):
        # 노드 이름을 'simple_subscriber'로 초기화
        super().__init__('simple_subscriber')
        # 'topic_name' 토픽을 구독. 메시지가 오면 listener_callback 실행
        self.subscription = self.create_subscription(
            String, 'topic_name', self.listener_callback, 10)

    def listener_callback(self, msg):
        # 받은 데이터를 터미널에 출력
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = SimpleSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
