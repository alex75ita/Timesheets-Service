import unittest
import pika
import threading
import time
from tests.integrationTests import consumers


class Consumer_test(unittest.TestCase):

    def test_startConsuming(self):

        def callback(channel, method, properties, body):
            print("callback")
            print(body)

        def connectionTimeoutCallback():
            print("connectionTimeoutCallback")

        def _closeChannel(channel_):
            print("_closeChannel")
            time.sleep(1)
            print("close")
            if channel_.is_open and not channel.is_closing:
                channel_.stop_consuming()
                print("stop_consuming")
            else:
                print("channel is closed")

        url = consumers.getUrl()
        queue = "test"
        params = pika.URLParameters(url)
        params.socket_timeout = 5
        connection = pika.BlockingConnection(params)
        connection.add_timeout(10, connectionTimeoutCallback)  # force to close
        channel = connection.channel()
        channel.basic_consume(callback,
                              queue=queue,
                              no_ack=True)

        t = threading.Thread(target=_closeChannel, args=[channel])
        t.start()

        print("start_consuming")
        channel.start_consuming()  # start consuming (loop)
        connection.close()
        print("end")
