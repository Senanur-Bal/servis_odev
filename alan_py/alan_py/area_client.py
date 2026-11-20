import sys
import rclpy
from rclpy.node import Node
from alan_interfaces.srv import RectangleArea


class RectangleAreaClient(Node):
    def __init__(self):
        super().__init__('rectangle_area_client')
        self.cli = self.create_client(RectangleArea, 'calculate_rectangle_area')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servis bekleniyor...')
        self.req = RectangleArea.Request()

    def send_request(self, width: float, height: float):
        self.req.width = width
        self.req.height = height
        future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) < 3:
        print('Kullanım: ros2 run alan_py area_client <width> <height>')
        sys.exit(1)

    try:
        width = float(sys.argv[1])
        height = float(sys.argv[2])
    except ValueError:
        print('Hata: width ve height sayısal (float) olmalıdır.')
        sys.exit(1)

    client = RectangleAreaClient()
    response = client.send_request(width, height)

    if response is not None:
        if response.success:
            client.get_logger().info(
                f'Alan ({width} x {height}) = {response.area}'
            )
        else:
            client.get_logger().error(
                f'İstek reddedildi! (width={width}, height={height})'
            )
    else:
        client.get_logger().error('Servis çağrısı başarısız oldu.')

    client.destroy_node()
    if rclpy.ok():
        rclpy.shutdown()


if __name__ == '__main__':
    main()
