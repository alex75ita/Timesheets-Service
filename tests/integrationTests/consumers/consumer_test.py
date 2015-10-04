import unittest
import pika
import threading
import time

_url = "amqp://rgryymew:5-V1Ax9_fTWtjIV9n1Jz_OOJ4hdbNlM3@baboon.rmq.cloudamqp.com/rgryymew"


class Consumer_test(unittest.TestCase):

    def test_startConsuming(self):

        def callback(channel, method, properties, body):
            print("callback")
            print(body)

        def connectionTimeoutCallback():
            print("connecionClosedCallback")

        def _closeChannel(channel_):
            print("_closeChannel")
            time.sleep(1)
            print("close")
            channel_.stop_consuming()
            #channel_.close()

        params = pika.URLParameters(_url)
        params.socket_timeout = 5
        connection = pika.BlockingConnection(params)
        connection.add_timeout(2, connectionTimeoutCallback)
        channel = connection.channel()
        channel.basic_consume(callback,
                              queue='test',
                              no_ack=True)

        t = threading.Thread(target=_closeChannel, args=[channel])
        t.start()

        print("start_consuming")
        channel.start_consuming()  # start consuming (blocks)
        connection.close()
        print("end")

#class ChannelCloseThread(threading.Thread):

