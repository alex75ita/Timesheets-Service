import unittest
import pika
import threading
import time
from consumers.consumerBase import ConsumerBase


class ConsumerBaseTest(unittest.TestCase):

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

    def test_startConsuming(self):

        #server = "bunny.cloudamqp.com"
        #user = "fkfpctoh"
        #password = "6yORM9AvfFYIhcv7pvO09GaTJsFvEpoi"
        url = "amqp://fkfpctoh:6yORM9AvfFYIhcv7pvO09GaTJsFvEpoi@bunny.cloudamqp.com/fkfpctoh"


        consumer = ConsumerBase(url)
        consumer.startConsuming()

